# arm-assembly-compile-script
a script made to ease the run of assembly on ARM based machines such as macbooks that use M1 chips.  It runs all compilation commands for you, just like you'd have with 'make' in C.

#PREREQUISITES

    python3 obviously
    a linux terminal (mac is the same)
    gcc (brew install gcc)
    xcode commandline

#USAGE

    comp [your asm.s file]

#EXAMPLES

    (Assuming you have a file named hello.s with only ARM based syntax)
    comp hello.s
    ./hello

you may use a windows shell/command prompt for this project too! just add it to your PATH as an alias then you're good to go.

#HOW TO USE

    clone the repository into your home directory, meaning Users/{your-name}
    ensure you get your files's exact root directory (you can have it using "find / -name "comp.py" 2>/dev/null" on the terminal [without the " ])
    cd to your ~./bash_profile or ~/.zshrc, which are both located in the root (meaning if you were in the {your-name} directory, do cd .. twice to reach top level)
    edit your bash profile or zshrc using nano {name from earlier} or sudo nano {name from earlier} if you face any permission erros.
    go to the last line, add this: alias cheat='python3 path/to/comp.py', then control O, enter, then control X to exit
    now use command line arguments to use the input for the compilation, as such: comp hello.s
    
