#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void factorize(int number) {
int i;
for (i = 2; i <= sqrt(number); i++) {
if (number % i == 0) {
printf("%d=%d*%d\n", number, i, number / i);
}
}
}

void factorize_file(const char* file_path) {
FILE* file = fopen(file_path, "r");
if (file == NULL) {
printf("Error opening file.\n");
exit(1);
}

char buffer[100];
while (fgets(buffer, sizeof(buffer), file)) {
int number = atoi(buffer);
factorize(number);
}

fclose(file);
}

int main(int argc, char* argv[]) {
if (argc != 2) {
printf("Usage: factors <file>\n");
return 1;
}

const char* file_path = argv[1];
factorize_file(file_path);

return 0;
}
