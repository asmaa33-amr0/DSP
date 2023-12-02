import numpy as np
import QuanTest2
import QuanTest1
def read_signal(filename):
    index = []
    sample = []

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                index.append(str(parts[0]))
                sample.append(float(parts[1]))

    return (index), sample
num_bits = int(input("Enter the number of bits: "))
num_levels = 2 ** num_bits
def quantize_signal(signal=[], num_levels=4):

    max_val = np.max(signal)
    min_val = np.min(signal)

    step_size = np.round((max_val - min_val) / num_levels,3)

    sorted_signal = sorted(signal)
    quantized_signal=[]
    mid_point=[]
    quantization_error=[]



    for i in  range(num_levels+1):

               quantized_signal .append (np.round( min_val +(step_size*i)  ,3))

    qq = []
    indexx=[]
    binary=[]
    final_mid=[]
    for i in range(num_levels + 1):



          if i< num_levels :
               qq.append([quantized_signal[i], quantized_signal[i + 1]])
               mid_point.append(np.round((quantized_signal[i]+quantized_signal[i+1])/2,3))
    for val in signal:
      for i in range(num_levels+ 1):
          if i <num_levels:
               if quantized_signal[i] <= val <= quantized_signal[i+1]:
                  quantization_error .append(np.round(mid_point[i] - val,3))
                  final_mid.append(mid_point[i])
                  indexx.append(i+1)
                  binary.append(format(i, '0{}b'.format(num_bits)))
    add_file = "Result.txt"
    with open(add_file, "w") as file:
        file.write(f"{0}\n")
        file.write(f"{0}\n")
        file.write(f"{len(signal)}\n")
        for i in range(len(signal)):
          file.write(f"{indexx[i]} {binary[i]} {final_mid[i]} {quantization_error[i]}\n")

    return indexx, binary,final_mid,quantization_error,add_file
input_file = input("Enter file name: ")
index, d = read_signal(input_file)
input_signal = np.array(d)


if input_file=="Quan2_input.txt":

   out_file="Quan2_Out.txt"
   indexx, binary, final_mid, quantization_error,filee = quantize_signal(input_signal, num_levels)
   QuanTest2.QuantizationTest2(out_file, indexx, binary, final_mid, quantization_error)
else :
    out_file = "Quan1_Out.txt"

    indexx, binary, final_mid, quantization_error,file = quantize_signal(input_signal, num_levels)
    binary, final_mid=read_signal(file)
    QuanTest1.QuantizationTest1(out_file, binary, final_mid)



