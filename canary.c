#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void hacked() {
    puts("YOU SHOULD NOT BE HERE!!!");
    system("/bin/sh");
}

void vuln() {
    char buffer[64];

    puts("Good luck getting past the stack protector...");
    gets(buffer);
    printf(buffer);

    puts("\nHmmmm I don't know what you're up to...");
    gets(buffer);
}

int main() {
    vuln();
}
