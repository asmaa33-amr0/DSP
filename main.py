
import numpy as np
import matplotlib.pyplot as plt
import comparesignals
import tkinter as tk
import QuanTest2
import QuanTest1
import  math

def read_signal_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

    signal_type = int(lines[0])
    is_periodic = int(lines[1])
    n1 = int(lines[2])

    data = [list(map(float, line.split())) for line in lines[3:]]

    return signal_type, is_periodic, n1, data


def quantize_signal(signal=[], num_levels=4 ,num_bits=2):
    max_val = np.max(signal)
    min_val = np.min(signal)

    step_size = np.round((max_val - min_val) / num_levels, 3)

    sorted_signal = sorted(signal)
    quantized_signal = []
    mid_point = []
    quantization_error = []

    for i in range(num_levels + 1):
        quantized_signal.append(np.round(min_val + (step_size * i), 3))

    qq = []
    indexx = []
    binary = []
    final_mid = []
    for i in range(num_levels + 1):

        if i < num_levels:
            qq.append([quantized_signal[i], quantized_signal[i + 1]])
            mid_point.append(np.round((quantized_signal[i] + quantized_signal[i + 1]) / 2, 3))
    for val in signal:
        for i in range(num_levels + 1):
            if i < num_levels:
                if quantized_signal[i] <= val <= quantized_signal[i + 1]:
                    quantization_error.append(np.round(mid_point[i] - val, 3))
                    final_mid.append(mid_point[i])
                    indexx.append(i + 1)
                    binary.append(format(i, '0{}b'.format(num_bits)))

    add_file = "Result.txt"
    with open(add_file, "w") as file:
        file.write(f"{0}\n")
        file.write(f"{0}\n")
        file.write(f"{len(signal)}\n")
        for i in range(len(signal)):
            file.write(f"{indexx[i]} {binary[i]} {final_mid[i]} {quantization_error[i]}\n")

    return indexx, binary, final_mid, quantization_error, add_file
def plot_continuous_signal(indices, samples, label="Continuous Signal"):
    plt.plot(indices, samples, label=label)
    plt.legend()
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.title('Signal Samples')
    plt.show()

def read_signal(filename):
    index = []
    sample = []

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                index.append(int(parts[0]))
                sample.append(float(parts[1]))

    return index, sample

def perform_operation():

    operation = var.get()

    if operation == 1:  # Addition
        def addition():

                file_path1 = entry1.get()

                file_path2 = entry2.get()
                signal_type1, is_periodic1, n1, data = read_signal_from_file(file_path1)

                index1, data1 = read_signal(file_path1)
                plot_continuous_signal( index1, data1,"First Signal")
                index2, data2 = read_signal(file_path2)
                plot_continuous_signal(index2, data2, "Second Signal")

                add = []
                for i in range(n1):
                    add.append(data1[i] + data2[i])

                add_file = "Result.txt"
                with open(add_file, "w") as file:
                    file.write(f"{signal_type1}\n")
                    file.write(f"{is_periodic1}\n")
                    file.write(f"{n1}\n")
                    for i in range(n1):
                        file.write(f"{i} {add[i]}\n")
                if file_path1 == 'Signal1.txt' and file_path2 == 'Signal2.txt':
                    filename = "Signal1+signal2.txt"
                elif file_path1 == 'Signal1.txt' and file_path2 == 'Signal3.txt':
                    filename = "Signal1+signal3.txt"
                ind,dataa=read_signal( add_file)
                plot_continuous_signal(ind,dataa,"Result Signal")
                index_list, sample_list = read_signal(filename)

                comparesignals.SignalSamplesAreEqual("Result.txt", index_list, sample_list)

        root = tk.Tk()

        # Set the window title
        root.title("Signal Addition")

        # Set the window size
        root.geometry("400x200")

        # Create a label and entry for the first signal file
        label1 = tk.Label(root, text="Signal 1:")
        label1.pack()

        entry1 = tk.Entry(root, width=40)
        entry1.pack()

        label2 = tk.Label(root, text="Signal 2:")
        label2.pack()

        entry2 = tk.Entry(root, width=40)
        entry2.pack()

        subtraction_button = tk.Button(root, text="Perform Addition", command=addition)
        subtraction_button.pack()

        # Start the main event loop
        root.mainloop()

    elif operation == 2:  # Subtraction


        def subtraction():
            file_path1 = entry1.get()
            file_path2 = entry2.get()

            signal_type1, is_periodic1, n1, data = read_signal_from_file(file_path1)
            index1, data1 = read_signal(file_path1)
            plot_continuous_signal(index1, data1,"First Signal")
            index2, data2 = read_signal(file_path2)
            plot_continuous_signal(index2, data2, "Second Signal")

            add = []
            for i in range(n1):
                add.append(data2[i] - data1[i])

            add_file = "Result.txt"
            with open(add_file, "w") as file:
                file.write(f"{signal_type1}\n")
                file.write(f"{is_periodic1}\n")
                file.write(f"{n1}\n")
                for i in range(n1):
                    file.write(f"{i} {add[i]}\n")
            if   file_path1 =='Signal1.txt' and file_path2 =='Signal2.txt' :
                filename = "Signal1-signal2.txt"
            elif file_path1 =='Signal1.txt' and file_path2 =='Signal3.txt' :
                filename = "Signal1-signal3.txt"
            index, data = read_signal(add_file)
            plot_continuous_signal(index, data, "Result Signal")
            index_list, sample_list = read_signal(filename)

            comparesignals.SignalSamplesAreEqual("Result.txt", index_list, sample_list)
        # Create the main window
        root = tk.Tk()

        # Set the window title
        root.title("Signal Subtraction")

        # Set the window size
        root.geometry("400x200")

        # Create a label and entry for the first signal file
        label1 = tk.Label(root, text="Signal 1:")
        label1.pack()

        entry1 = tk.Entry(root, width=40)
        entry1.pack()

        label2 = tk.Label(root, text="Signal 2:")
        label2.pack()

        entry2 = tk.Entry(root, width=40)
        entry2.pack()

        subtraction_button = tk.Button(root, text="Perform Subtraction", command=subtraction)
        subtraction_button.pack()

        # Start the main event loop
        root.mainloop()


        # Display success message

    elif operation == 3:  # Multiplication
        def multt():
            constt = int(entry1.get())
            file_path2 = entry2.get()

            signal_type1, is_periodic1, n1, data = read_signal_from_file(file_path2)
            index1, data1 = read_signal(file_path2)
            plot_continuous_signal(index1, data1," Oregnal Signal ")

            mult = []
            for i in range(n1):
                mult.append(int(constt)*int(data1[i]))

            add_file = "Result.txt"
            with open(add_file, "w") as file:
                file.write(f"{signal_type1}\n")
                file.write(f"{is_periodic1}\n")
                file.write(f"{n1}\n")
                for i in range(n1):
                    file.write(f"{i} {mult[i]}\n")
            if file_path2 == 'Signal1.txt':
                filename = "MultiplySignalByConstant-Signal1 - by 5.txt"
            elif file_path2 == 'Signal2.txt':
                filename = "MultiplySignalByConstant-Signal2 - by 10.txt"
            index, data = read_signal(add_file)
            plot_continuous_signal(index, data, " Signal after Multiplication")
            index_list, sample_list = read_signal(filename)

            comparesignals.SignalSamplesAreEqual("Result.txt", index_list, sample_list)
            # Create the main window

        root = tk.Tk()

        # Set the window title
        root.title("Signal Multiplication")

        # Set the window size
        root.geometry("400x200")

        # Create a label and entry for the first signal file
        label1 = tk.Label(root, text="constant:")
        label1.pack()

        entry1 = tk.Entry(root, width=40)
        entry1.pack()

        label2 = tk.Label(root, text="Signal :")
        label2.pack()

        entry2 = tk.Entry(root, width=40)
        entry2.pack()

        subtraction_button = tk.Button(root, text="Perform multiplication", command= multt)
        subtraction_button.pack()

        # Start the main event loop
        root.mainloop()

    elif operation == 4:  # Squaring
        def Squaring():

            file_path1 = entry1.get()

            signal_type1, is_periodic1, n1, data = read_signal_from_file(file_path1)
            index1, data1 = read_signal(file_path1)
            plot_continuous_signal(index1, data1, " Oregnal Signal")

            add = []

            for i in range(n1):

                add.append(int( data1[i]*data1[i]))

            add_file = "Result.txt"
            with open(add_file, "w") as file:
                file.write(f"{signal_type1}\n")
                file.write(f"{is_periodic1}\n")
                file.write(f"{n1}\n")
                for i in range(n1):
                    file.write(f"{i} {add[i]}\n")
            ind,dataa=read_signal(add_file)
            plot_continuous_signal(ind,dataa,"Signal Squaring")
            if file_path1 == 'Signal1.txt':
                filename = "Output squaring signal 1.txt"
            elif file_path1 == 'Signal2.txt':
                filename = "Output squaring signal 2.txt"

            index_list, sample_list = read_signal(filename)

            comparesignals.SignalSamplesAreEqual("Result.txt", index_list, sample_list)

        root = tk.Tk()

        # Set the window title
        root.title("Signal Squaring")

        # Set the window size
        root.geometry("400x200")

        # Create a label and entry for the first signal file
        label1 = tk.Label(root, text="Signal :")
        label1.pack()

        entry1 = tk.Entry(root, width=40)
        entry1.pack()


        subtraction_button = tk.Button(root, text="Perform Squaring", command=Squaring)
        subtraction_button.pack()

        # Start the main event loop
        root.mainloop()


    elif operation == 5:  # Shifting
        def Shifting():
            constt = int(entry1.get())
            file_path1 = entry2.get()

            signal_type1, is_periodic1, n1, data = read_signal_from_file(file_path1)
            index1, data1 = read_signal(file_path1)
            plot_continuous_signal(index1, data1, " Oregnal Signal")

            Shifted = []
            index11=[]

            for i in range(n1):

                Shifted.append((data1[i]))
                index11.append(( index1[i] +constt ))

            add_file = "Result.txt"
            with open(add_file, "w") as file:
                file.write(f"{signal_type1}\n")
                file.write(f"{is_periodic1}\n")
                file.write(f"{n1}\n")
                for i in range(n1):
                    file.write(f"{index11[i]} {Shifted[i]}\n")
            index1, data1 = read_signal(add_file)
            plot_continuous_signal(index1, data1, " Shifted Signal")
            if  constt>0:
                filename = "output shifting by add 500.txt"
            elif constt<0:
                filename = "output shifting by minus 500.txt"

            index_list, sample_list = read_signal(filename)

            comparesignals.SignalSamplesAreEqual("Result.txt", index_list, sample_list)

        root = tk.Tk()

        # Set the window title
        root.title("Signal Shifting")

        # Set the window size
        root.geometry("400x200")


        label1 = tk.Label(root, text=" Enter Shifting value")
        label1.pack()

        entry1 = tk.Entry(root, width=40)
        entry1.pack()

        label2 = tk.Label(root, text="Signal :")
        label2.pack()

        entry2 = tk.Entry(root, width=40)
        entry2.pack()

        Perform_button = tk.Button(root, text="Perform Shifting", command=Shifting)
        Perform_button.pack()

        # Start the main event loop
        root.mainloop()


    elif operation == 6:  # Normalization


        def Normalization():
            constt = int(entry1.get())
            file_path1 = entry2.get()

            signal_type1, is_periodic1, n1, data = read_signal_from_file(file_path1)
            index1, data1 = read_signal(file_path1)
            plot_continuous_signal(index1, data1,"Oregnal Signal")
            Normalized = []
            mini=min(data1)
            maxx=max(data1)
            for i in range(n1):
                if constt==1:
                  Normalized.append( (data1[i] - mini) / (maxx - mini))
                else:
                    Normalized.append( (data1[i] - mini) / (maxx - mini) * 2 - 1)

            add_file = "Result.txt"
            with open(add_file, "w") as file:
                file.write(f"{signal_type1}\n")
                file.write(f"{is_periodic1}\n")
                file.write(f"{n1}\n")
                for i in range(n1):
                    file.write(f"{i} {Normalized[i]}\n")
            if file_path1 == 'Signal1.txt'  :
                filename = "normalize of signal 1 -- output.txt"
            elif   file_path1 == 'Signal2.txt':
                filename = "normlize signal 2 -- output.txt"
            index, data = read_signal(add_file)
            plot_continuous_signal(index, data, "Normalized Signal")
            index_list, sample_list = read_signal(filename)

            comparesignals.SignalSamplesAreEqual("Result.txt", index_list, sample_list)

        root = tk.Tk()

        # Set the window title
        root.title("Signal Normalization")

        # Set the window size
        root.geometry("400x200")

        # Create a label and entry for the first signal file
        label1 = tk.Label(root, text="1 to (0:1) , 2  to (-1:1)")
        label1.pack()

        entry1 = tk.Entry(root, width=40)
        entry1.pack()



        # Create a label and entry for the second signal file
        label2 = tk.Label(root, text="Signal :")
        label2.pack()

        entry2 = tk.Entry(root, width=40)
        entry2.pack()


        Perform_button = tk.Button(root, text="Perform Normalization", command=Normalization)
        Perform_button.pack()

        # Start the main event loop
        root.mainloop()

    elif operation == 7:  # Accumulation
        def Accumulation():

            file_path1 = entry1.get()

            signal_type1, is_periodic1, n1, data = read_signal_from_file(file_path1)
            index1, data1 = read_signal(file_path1)
            plot_continuous_signal(index1, data1, "Oregnal Signal")

            add = []
            sum=0
            for i in range(n1):
                sum+=data1[i]
                add.append(int(sum))

            add_file = "Result.txt"
            with open(add_file, "w") as file:
                file.write(f"{signal_type1}\n")
                file.write(f"{is_periodic1}\n")
                file.write(f"{n1}\n")
                for i in range(n1):
                    file.write(f"{i} {add[i]}\n")
            if file_path1 == 'Signal1.txt'  :
                filename = "output accumulation for signal1.txt"
            elif   file_path1 == 'Signal3.txt':
                filename = "output accumulation for signal1.txt"
            index, data = read_signal(add_file)
            plot_continuous_signal(index, data, " Signal after accumulation ")
            index_list, sample_list = read_signal(filename)

            comparesignals.SignalSamplesAreEqual("Result.txt", index_list, sample_list)

        root = tk.Tk()

        # Set the window title
        root.title("Signal Accumulation")

        # Set the window size
        root.geometry("400x200")


        label1 = tk.Label(root, text="Signal :")
        label1.pack()

        entry1 = tk.Entry(root, width=40)
        entry1.pack()

        Perform_button = tk.Button(root, text="Perform Accumulation", command=Accumulation)
        Perform_button.pack()

        root.mainloop()

    elif operation == 8: #generate_signal

        def generate_signal(wave_type, amplitude, phase_shift, analog_freq, sampling_freq):


            num_samples = sampling_freq
            time_values = np.arange(num_samples) / sampling_freq
            if wave_type.lower() == 'sin':
                signal_type = 0
                amplitude_values = amplitude * np.sin(2 * np.pi * analog_freq * time_values + phase_shift)
            elif wave_type.lower() == 'cos':
                signal_type = 0
                amplitude_values = amplitude * np.cos(2 * np.pi * analog_freq * time_values + phase_shift)


            time_domain = 0
            is_periodic = 0

            # Create the output file
            with open("Result.txt", "w") as file:
                file.write(f"{signal_type}\n")
                file.write(f"{is_periodic}\n")
                file.write(f"{num_samples}\n")

                for i in range(num_samples):
                    amplitude_values[i] = round(amplitude_values[i], 6)
                    file.write(f"{i} {amplitude_values[i]}\n")

        def handle_button_click():
            wave_type = entry1.get()
            amplitude = int(entry2.get())
            phase_shift = float(entry3.get())
            analog_freq = int(entry4.get())
            sampling_freq = int(entry5.get())

            generate_signal(wave_type, amplitude, phase_shift, analog_freq, sampling_freq)
            index,data=read_signal("Result.txt")
            plot_continuous_signal(index,data,"generated Signal")
            if wave_type == 'sin':
                filename = "SinOutput .txt"
            elif  wave_type == 'cos':
                filename = "CosOutput .txt"

            index_list, sample_list = read_signal(filename)

            comparesignals.SignalSamplesAreEqual("Result.txt", index_list, sample_list)

        root = tk.Tk()
        # Set the window title
        root.title("Task 1 generate")

        # Set the window size
        root.geometry("500x250")

        # Create a label and entry for the first signal file
        label1 = tk.Label(root, text="Signal type:")
        label1.pack()

        entry1 = tk.Entry(root, width=40)
        entry1.pack()

        # Create a label and entry for the second signal file
        label2 = tk.Label(root, text="amplitude:")
        label2.pack()

        entry2 = tk.Entry(root, width=40)
        entry2.pack()
        label3 = tk.Label(root, text="phase_shift:")
        label3.pack()

        entry3 = tk.Entry(root, width=40)
        entry3.pack()
        label4 = tk.Label(root, text="analog_freq:")
        label4.pack()

        entry4 = tk.Entry(root, width=40)
        entry4.pack()
        label5 = tk.Label(root, text="sampling_freq:")
        label5.pack()

        entry5 = tk.Entry(root, width=40)
        entry5.pack()

        subtraction_button = tk.Button(root, text="generate_signal", command=handle_button_click)
        subtraction_button.pack()

        root.mainloop()
    elif operation == 9:

        def Quantize():
            choice = int(entry1.get())
            num_bits_or_level = int(entry2.get())
            input_file = entry3.get()

            if choice == 1:
                num_bits = num_bits_or_level
                num_levels=2** num_bits
            else:
                num_levels = num_bits_or_level
                num_bits = math.log(num_levels, 2)
            num_bits = int(num_bits)
            index, d = read_signal(input_file)
            input_signal = np.array(d)

            if input_file == "Quan2_input.txt":
                out_file = "Quan2_Out.txt"
                indexx, binary, final_mid, quantization_error, filee = quantize_signal(input_signal, num_levels,num_bits
                                                                                          )
                QuanTest2.QuantizationTest2(out_file, indexx, binary, final_mid, quantization_error)
            else:
                out_file = "Quan1_Out.txt"
                indexx, binary, final_mid, quantization_error, file = quantize_signal(input_signal, num_levels,num_bits
                                                                                       )
                binary, final_mid = read_signal(file)
                QuanTest1.QuantizationTest1(out_file, binary, final_mid)
            plot_continuous_signal(indexx,final_mid,"Quantized Signal")

        root = tk.Tk()

        # Set the window title
        root.title("Signal Quantization")

        # Set the window size
        root.geometry("400x200")

        # Create a label and entry for the first signal file
        label1 = tk.Label(root, text="1 for bits, 2 for levels")
        label1.pack()

        entry1 = tk.Entry(root, width=40)
        entry1.pack()

        # Create a label and entry for the second signal file
        label2 = tk.Label(root, text="bits_or_level")
        label2.pack()

        entry2 = tk.Entry(root, width=40)
        entry2.pack()

        label3 = tk.Label(root, text="Signal")
        label3.pack()

        entry3 = tk.Entry(root, width=40)
        entry3.pack()

        Perform_button = tk.Button(root, text="Perform Quantization", command=Quantize)
        Perform_button.pack()

        # Start the main event loop
        root.mainloop()

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Arithmetic Operations")

# Set the window size
root.geometry("600x500")

# Create a label to display the available operations
label = tk.Label(root, text="Arithmetic Operations Menu:", font=("Arial", 14, "bold"))
label.pack()

# Create a variable to hold the selected operation
var = tk.IntVar()

# Create radio buttons for each operation
operations = [
    "Addition",
    "Subtraction",
    "Multiplication",
    "Squaring",
    "Shifting",
    "Normalization",
    "Accumulation",
    "Go to task 1",
    "Quantization"
]
for i, operation in enumerate(operations):
    radio_button = tk.Radiobutton(root, text=operation, variable=var, value=i+1, font=("Arial", 12))
    radio_button.pack(anchor=tk.W)
# Create a button to perform the selected operation
operation_button = tk.Button(root, text="Perform Operation", command=perform_operation)
operation_button.pack()

# Start the main event loop
root.mainloop()


