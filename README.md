# FieldVoles
Commands and scripts used in the Field vole paper

1. Multidimensional Scaling Plot
 - Compute identiti-by-state matrix:
time -p  ${angsd}/angsd  -minMapQ 25 -minQ 25 -uniqueOnly 1 -remove_bads 1  -nThreads 4  -GL 2 -doGlf 2 -doMajorMinor 1 -doMaf 2 -SNP_pval 1e-6 -doIBS 1 -doCounts 1  -makeMatrix 1 -doCov 1 -out AGR_MDS_MicOch -minFreq 0.08 -rmTrans 1 -minInd 25  -rf /path/MicOch_1Mscaf_nosex.txt -bam /path/AGR_BAMS_MicOch_noOut.txt



2. Heterozygosity:
 - Compute SAF files:
time -p ${angsd}/angsd -i '/path/input.bam' -anc '/path/M_agrestis_GCA_902806775_genomic_MT.fa' -dosaf 1 -fold 1 -rf '/path/AGRnuc_contigs_noXY_100kb.txt' -out  ${i%_AGRnuc_merged_nodup_realign.bam}.het -gl 2  -minQ 20 -minmapq 25 -skiptriallelic 1 -uniqueonly 1 -setMinDepthInd 5 -doMajorMinor 1
 - Compute folded SFS:
