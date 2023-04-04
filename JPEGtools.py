# @AmirMehrabian March 4 2023

import numpy as np
from scipy.stats import entropy
from scipy.fftpack import dct, idct


def entropy_2d(image,levels):
    hist,_ = np.histogram(image.ravel(),levels)
    return entropy(hist, base = 2)


def DCT2(input_image):
    output = dct(dct(input_image, axis=0, norm='ortho'), axis=1, norm='ortho')
    return output


def iDCT2(input_image):
    output = idct(idct(input_image, axis=0, norm='ortho'), axis=1, norm = 'ortho')
    return output


def cal_category(input_level):

      if -1 <= input_level and input_level <= 1:
        category = 1

      elif -3 <= input_level and input_level <= 3:
        category = 2

      elif -7 <= input_level and input_level <= 7:
        category = 3

      elif -15 <= input_level and input_level <= 15:
        category = 4

      elif -31 <= input_level and input_level <= 31:
        category = 5

      elif -63 <= input_level and input_level <= 63:
        category = 6

      elif -127 <= input_level and input_level <= 127:
        category = 7

      elif -255<= input_level and input_level <= 255:
        category = 8

      elif -511 <= input_level and input_level <= 511:
        category = 9

      elif -1023 <= input_level and input_level <= 1023:
        category = 10

      elif -2047 <= input_level and input_level <= 2047:
        category = 11

      return category


def twos_complement(input):
    # Convert binary number to integer
    binary_num = format(input, "b")
    num_bits = len(binary_num)

    # Calculate two's complement
    two_complement = 2**num_bits - input
    
    # Convert result back to binary
    logarithm = np.log2(input)

    if logarithm.is_integer():
      binary_result = (num_bits-1)*'0'
    
    else:
      binary_result = format(two_complement, f"0{num_bits}b")
    
    return binary_result


def symbol2(level):
  
    if level >= 0:
        output = format(level, "b")
    else:
        output = twos_complement(abs(level-1))

    return output


def run_cat_level(input_block):
    zigzag_indx = np.array([ 0,  1,  8,  16,  9,  2,  3,  10,
                            17, 24, 32,  25, 18, 11,  4,   5,
                            12, 19, 26,  33, 40, 48, 41,  34,
                            27, 20, 13,   6,  7, 14, 21,  28,
                            35, 42, 49,  56, 57, 50, 43,  36,
                            29, 22, 15,  23, 30, 37, 44,  51,     
                            58, 59, 52,  45, 38, 31, 39,  46,
                            53, 60, 61,  54, 47, 55, 62,  63])
    
    zigzag_seq = input_block.ravel()[zigzag_indx]


    run_level = np.zeros([0,3])   
    counter = 0 
    for element in zigzag_seq:
      if element == 0:
          counter += 1
      else:
          run_level = np.concatenate([run_level, 
                                      np.array([counter, cal_category(element), element]).reshape(1,3)],
                                     axis = 0)
          counter = 0
    run_level = np.concatenate([run_level, np.array([0, 0, 0]).reshape(1,3)], axis = 0)

    return run_level.astype(int)
      
    
def block_huffman_encoder(r_c_l, codebook):

    encoded_block = {}

    for ii, rcl in enumerate(r_c_l):
      if ii == 0:
        sym1 = codebook['DC'][str(rcl[1])]
        
      else:
        sym1 = codebook['AC'].get((rcl[0],rcl[1]))
      

      if rcl[0]> 15:
        sym1 =''
        for jj in range(rcl[0]//16):
            sym1 = sym1 + codebook['AC'].get((15, 0))+' '
        sym1 = sym1 + codebook['AC'].get((rcl[0]%16,rcl[1]))
        
      code = sym1 + ' ' + str(symbol2(rcl[2]))


      encoded_block[str(ii)] = code

    return encoded_block


def size_in_bits(encoded_image):

    num_bits = 0

    for key_block in encoded_image.keys():
      for key_element in encoded_image[key_block].keys():

          code_item = encoded_image[key_block][key_element]
          num_bits = num_bits + len(code_item) -1

    return num_bits

