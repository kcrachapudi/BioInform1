#!/bin/bash

echo "Starting BioInform1 NGS Pipeline..."

echo "Step1: Quality Control"
fastqc ../data/sample.fastq -o ../results

echo "Step2: Indexing Reference Genome"
bwa index ../reference/reference.fa

echo "Step3: Aligning Reads"
bwa mem ../reference/reference.fa ../data/sample.fastq > ../results/aligned.sam

echo "Step4: Convert SAM to BAM"
samtools view -Sb ../results/aligned.sam > ../results/aligned.bam

echo "Step5: Sorting BAM"
samtools sort ../results/aligned.bam -o ../results/aligned_sorted.bam

echo "BioInform1 Pipeline Completed"
