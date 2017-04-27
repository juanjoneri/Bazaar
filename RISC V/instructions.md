# Written report of my experience with this installation

## Commands Used for installation
> Available at RISC-V Tools (GNU Toolchain, ISA Simulator, Tests) [github repo](https://github.com/riscv/riscv-tools)

### Operating System Check
For the configuration of the RISC-V (pronounced “risk-five”) software instruction set architecture (ISA), and in order to get it running on my computer I used *Oracle's VM virtual box* running an image of the 16_04_02 version of Ubuntu (Xenial Xerus) available at the [archive](http://releases.ubuntu.com/16.04/) of Ubuntu's community website.

> Whether you’re an experienced technology user or you’re just getting started, there are lots of ways to get involved with the Ubuntu community. Ubuntu is more than an operating system for your computer, server, cloud, phone, tablet, or TV. It’s also a massively collaborative project. Ubuntu is always open and looking for ways to create the best possible experience for anyone who tries it and community participation is a great way to help make that happen.

Using the following built in command found in this Linux distribution I was able to determine the exact specifications of the system used to run this project and redirect it to a file for future reference. This can be found in the project [attachments](./system_specs.txt).
```bash
sudo lshw > system_specs.txt
```

### Set up the directory

```bash
pwd
cd Desktop/
mkdir RiscV
cd RiscV/
export TOP=$(pwd)
```

### GCC Version

Check that `GCC --version` is newer than 4.8 for C++11 support (including thread_local).

### Obtaining and Compiling the Sources (7.87 SBU)

clone the tools from the *riscv-tools* GitHub repository:
```bash
git clone https://github.com/riscv/riscv-tools.git
```

This command will bring in only references to the repositories that we will need. It took 137 minutes in my computer
```bash
cd $TOP/riscv-tools
git submodule update --init --recursive
```

Install other packages to build GCC, including flex, bison, autotools, libmpc, libmpfr, and libgmp. This step took 2 minutes.
I also had to give super user permission to the system to perform the command
```bash
sudo apt-get install autoconf automake autotools-dev curl libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo gperf libtool patchutils bc
```

Set the $RISCV environment variable. The variable is used throughout the build script process to identify where to install the new tools.
```bash
export RISCV=$TOP/riscv
export PATH=$PATH:$RISCV/bin
```

With everything else set up, run the build script.
```bash
./build.sh
```

After error try `sudo ./build.sh`
And the error still `Please set the RISCV environment variable to you preferred install path`
Maybe because I turned off the computer in the middle of the process

```bash
cd RiscV/
export TOP=$(pwd)
cd $TOP/riscv-tools
export RISCV=$TOP/riscv
export PATH=$PATH:$RISCV/bin
cd ..
```

This solved the issue in 23 minutes.
Because I needed to repeat this process every time I rebooted the system to continue with the assignment, I decided to write a bash script that would automate the process for me.

First open nano editor:
```bash
nano setup.sh
```

Write the script
```bash
export TOP=$(pwd)
cd $TOP/riscv-tools
export RISCV=$TOP/riscv
export PATH=$PATH:$RISCV/bin
cd ..
echo "all setup!"
```

Press <kbd>Ctr</kbd> + <kbd>x</kbd> to save and exit the program
And then <kbd>y</kbd> to accept

### Testing that all is working
Write the program

```bash
cd $TOP
echo -e '#include <stdio.h>\n int main(void) { printf("Hello world!\\n"); return 0; }' > hello.c
```

Build the program with `riscv64-unknown-elf-gcc -o hello hello.c`

When you're done, you may think to do ./hello, but not so fast. We can't even run spike hello, because our "Hello world!" program involves a system call, which couldn't be handled by our host x86 system. We'll have to run the program within the proxy kernel, which itself is run by spike, the RISC-V architectural simulator. Run this command to run your "Hello world!" program:

run using `spike pk hello`

The RISC-V architectural simulator, spike, takes as its argument the path of the binary to run. This binary is pk, and is located at $RISCV/riscv-elf/bin/pk. spike finds this automatically. Then, riscv-pk receives as its argument the name of the program you want to run.

### Running code

using the command `riscv64-unknown-elf-gcc --help > riscv64_help.txt` I redirected the output of the help command to find out more about the functionality of risc V compiler. The file was named [riscv64_help.txt](./riscv64_help.txt) and can be found in the attachments. Specifically, I found an option for saving temporary files created in the different stages of c compilation `-save-temps`.

- *preprocessing* generated a hello.i file
- *compilation* generated hello.s file, containing the generated assembly instructions.
- *assembly* generated hello.o
- *linking* generated hello, an executable program
