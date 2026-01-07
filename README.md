[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

# Field voles - genomics
This repository contains commands and scripts used in the analyses presented in: 

Baca M, Bujalska B, Popović D, Golubiński M, Alves PC, Bard E, Berto C, Cuenca-Bescós G, Dalén L, Fewlass H, Fadeeva T, Herman J, Horáček I, Krajcarz M, Law M, Lemanik A, López-García JM, Luzi L, Murelaga X, Mahmoudi A, Peresani M, Parfitt S, Pauperio J, Pavlova SV, Pazonyi P, Rodríguez IR, Searle JB, Stojak J, Strukova T, Wójcik JM, Nadachowski A. The evolutionary history of the field vole species complex revealed by modern and ancient genomes. 2025 Genome Biology


1. Multidimensional Scaling Plot
 - Compute identiti-by-state matrix:
	time -p  ${angsd}/angsd  -minMapQ 25 -minQ 25 -uniqueOnly 1 -remove_bads 1  -nThreads 4  -GL 2 -doGlf 2 -doMajorMinor 1 -doMaf 2 -SNP_pval 1e-6 -doIBS 1 -doCounts 1  -makeMatrix 1 -doCov 1 -out AGR_MDS_MicOch -minFreq 0.08 -rmTrans 1 -minInd 25  -rf /path/MicOch_1Mscaf_nosex.txt -bam /path/AGR_BAMS_MicOch_noOut.txt

IBS matrix was visualised as a MDS plot using cmdscale and ggplot functions in R.  

2. Generate SNP dataset: 

 - Generate GLs and MAFs for a set of modern samples:
 
 	time -p  ${angsd}/angsd -bam /path/AGR_BAMS_MicOch_modern_out.txt -doCounts 1  -minMapQ 25 -minQ 30  -uniqueOnly 1 -remove_bads 1  -nThreads 4  -GL 2 -doGlf 2 -doMajorMinor 1 -doMaf 2 -minMaf 0.05 -rmTrans 1  -minInd 15   -setMinDepth 90  -setMaxDepth 600 -skipTriallelic 1 -out AGR_MicOch_GL_modern_out -rf /path/MicOch_1Mscaf_nosex.txt

 - Generate .sites file from mafs file:  

	pigz -dc  xxx.mafs.gz |awk 'FNR>1 {print $1, $2}'>file.sites

 - index sites file:
 
	${angsd}/angsd sites index file.sites
 
- Run angsd haplocall for the selected sites on all samples 

	time -p  ${angsd}/angsd -minMapQ 25 -minQ 25  -uniqueOnly 1 -remove_bads 1   -doHaploCall 1 -minMinor 2  -maxMis 3  -doCounts 1  -nThreads 4 -out AGR_MicOch_haplo_sites_out    -sites file.sites  -bam /path/AGR_BAMS_MicOch_Out.txt

 - The initial GL command contained -skiptriallelic and - rmTrans options but as more   samples are used in all samples haplocall triallelic sites and transitions appears in the output. Filter resulting haplo.gz file using 2AllelesFilter_gzip.py and CDeaminationFilter_gzip.py to remove them.

 - convert 'haplo.gz' file to plink's tped/tfam format using haploToplink script from Angsd/misc/ folder. 
 
 	${angsd}/misc/haploToplink yourfile_haplo.gz plink_file_steam
 
4. Generate input file and run TreeMix:

 - Convert plink to treemix format:
 		- generate cluster file:
			./plink -tfile  plink_steam --write-cluster --family --allow-extra-chr -out out_steam --missing-genotype N
 
3. Heterozygosity:
 - Compute SAF files:
	time -p ${angsd}/angsd -i '/path/input.bam' -anc '/path/M_agrestis_GCA_902806775_genomic_MT.fa' -dosaf 1 -fold 1 -rf '/path/AGRnuc_contigs_noXY_100kb.txt' -out  ${i%_AGRnuc_merged_nodup_realign.bam}.het -gl 2  -minQ 20 -minmapq 25 -skiptriallelic 1 -uniqueonly 1 -setMinDepthInd 5 -doMajorMinor 1
 - Compute folded SFS:

5. AdmixtureBayes:


