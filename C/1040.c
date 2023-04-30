#include <math.h>
#include <stdio.h>

int main() {

  float n1, n2, n3, n4, media, exm, mf;

  scanf("%f", &n1);
  scanf("%f", &n2);
  scanf("%f", &n3);
  scanf("%f", &n4);

  media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10;
  printf("Media: %.1f\n", media);

  if (media >= 7) {
    printf("Aluno aprovado.\n");
  }
  else if (media < 5) {
    printf("Aluno reprovado.\n");
  } else {
    printf("Aluno em exame.\n");
    scanf("%f", &exm);
    mf = (media + exm) / 2;
    if (mf >= 5) {
      printf("Nota do exame: %.1f\n", exm);
      printf("Aluno aprovado.\n");
      printf("Media final: %.1f\n", (mf));
    } else {
      printf("Nota do exame: %.1f\n", exm);
      printf("Aluno reprovado\n");
      printf("Media final: %.1f\n", (mf));
    }
  }
  return 0;
}