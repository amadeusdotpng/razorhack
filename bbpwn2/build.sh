gcc -D_GNU_SOURCE -static -static-libgcc -static-libstdc++ -fno-stack-protector -no-pie main.c -o main -lm