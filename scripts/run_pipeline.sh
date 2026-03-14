CONFIG=../config/config.txt

source $CONFIG

echo "Starting BioInform1 Pipeline" | tee -a $LOG

echo "Step 1: Quality Control" | tee -a $LOG
fastqc $FASTQ -o $OUTPUT >> $LOG 2>&1

echo "Step 2: Indexing Reference Genome" | tee -a $LOG
bwa index $REFERENCE >> $LOG 2>&1

echo "Step 3: Aligning Reads" | tee -a $LOG
bwa mem $REFERENCE $FASTQ > $OUTPUT/aligned.sam 2>> $LOG

echo "Step 4: Convert SAM to BAM" | tee -a $LOG
samtools view -Sb $OUTPUT/aligned.sam > $OUTPUT/aligned.bam 2>> $LOG

echo "Step 5: Sorting BAM" | tee -a $LOG
samtools sort $OUTPUT/aligned.bam -o $OUTPUT/aligned_sorted.bam 2>> $LOG

echo "Pipeline Completed Successfully" tee -a $LOG

