# Project Overview

BioInform1 is a simplified Next Generation Sequencing (NGS) data
processing pipeline that demonstrates how raw genomic sequencing data is
transformed into aligned genomic data suitable for downstream analysis.
The pipeline performs quality control, sequence alignment, and genomic
file transformation using standard bioinformatics tools.

# Pipeline Architecture

Pipeline Flow:\
FASTQ → Quality Control → Alignment → SAM → BAM → Sorted BAM\
\
Tools Used:\
- FastQC: Quality control of sequencing reads\
- BWA: Alignment of DNA reads to reference genome\
- Samtools: Processing and transformation of alignment files

# Technical Workflow

## Step 1 -- FASTQ Input

FASTQ files store raw sequencing reads produced by sequencing machines.
Each read includes the DNA sequence and a quality score for every base.

## Step 2 -- Quality Control (FastQC)

FastQC analyzes sequencing quality including base quality scores, GC
content, sequence duplication levels, and potential sequencing biases.

## Step 3 -- Reference Genome Indexing

The reference genome must be indexed so the alignment tool can quickly
search for matching sequences. BWA creates index files used to map reads
efficiently.

## Step 4 -- Sequence Alignment

Alignment maps sequencing reads to their position in a reference genome.
This allows identification of where each DNA fragment originates within
the genome.

## Step 5 -- SAM to BAM Conversion

SAM is a human-readable alignment format. BAM is the compressed binary
version used for efficient storage and computation.

## Step 6 -- Sorting BAM Files

Sorting organizes reads based on genomic coordinates, enabling efficient
querying and preparation for downstream analysis such as variant
detection.

# Genetics Perspective

From a biological perspective, the pipeline converts raw sequencing
fragments into genomic coordinates mapped to a reference genome. Once
aligned, researchers can identify genetic mutations, variants, and
structural differences in DNA.
