# JPEG-Image-Encoding
This repository contains code for implementation of JPEG based on [1][2]. It performs blocking of the image, DCT transform, quantization, zigzag scan, categorization, DC difference, run-level encoding, and entropy coding to achieve image compression.\
The notebook "**JPEG_Image_Encoding_and_Compression.ipynb**" contains the implementation of JPEG compression. The amount of compression is determined by the scaler variable. A larger scaler value results in a more blocky image with fewer details but better compression.\
The Huffman encoding table is stored in the "**codebook.npy**" file. The "**JPEGtools.py**" module contains the necessary functions for the JPEG compression algorithm.

## **Results**
The script compresses the input image and compares the size and quality of the original and compressed images. 

## **Dependencies**
numpy\
scipy\
scikit-image

## **References**
[1] I. E. Richardson, Video Codec Design: Developing Image and Video Compression Systems. Wiley, 2002.\
[2] M. Ghanbari and I. o. E. Engineers, Standard Codecs: Image Compression to Advanced Video Coding. Institution of Engineering and Technology, 2003.
