#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void load_pcm(const char *filename, float *buffer, size_t size) {
    FILE *file = fopen(filename, "rb");
    if (!file) {
        printf("Erro ao abrir o arquivo %s\n", filename);
        exit(EXIT_FAILURE);
    }
    fread(buffer, sizeof(float), size, file);
    fclose(file);
}

void save_pcm(const char *filename, float *buffer, size_t size) {
    FILE *file = fopen(filename, "wb");
    if (!file) {
        printf("Erro ao salvar o arquivo %s\n", filename);
        exit(EXIT_FAILURE);
    }
    fwrite(buffer, sizeof(float), size, file);
    fclose(file);
}

void lms_algorithm(float *x, float *d, float *e, float *w, int N, int M, float u) {
    float y;
    int n, k;

    for (n = M; n < N; n++) {
        y = 0.0;

        // Calcular a saída do filtro
        for (k = 0; k < M; k++) {
            y += w[k] * x[n - k];
        }

        // Calcular o erro
        e[n] = d[n] - y;

        // Atualizar os coeficientes do filtro
        for (k = 0; k < M; k++) {
            w[k] += 2.0f * u * e[n] * x[n - k];
        }
    }
}

int main() {
    // Parâmetros do LMS
    const int N = 40000; // Número de amostras
    const int M = 8;     // Tamanho do filtro adaptativo
    const float u = 0.05f; // Passo de adaptação

    // Buffers para os sinais
    float *x = (float *)malloc(N * sizeof(float));
    float *d = (float *)malloc(N * sizeof(float));
    float *e = (float *)malloc(N * sizeof(float));
    float *w = (float *)calloc(M, sizeof(float)); // Inicializar coeficientes com zero

    if (!x || !d || !e || !w) {
        printf("Erro ao alocar memória\n");
        exit(EXIT_FAILURE);
    }

    // Carregar os sinais x[n] e d[n]
    load_pcm("ruido_branco.pcm", x, N);
    load_pcm("dn_Q1.pcm", d, N);

    // Executar o algoritmo LMS
    lms_algorithm(x, d, e, w, N, M, u);

    // Salvar o sinal de erro
    save_pcm("erro_Q1_C.pcm", e, N);

    // Liberar memória
    free(x);
    free(d);
    free(e);
    free(w);

    printf("Processamento concluído. Sinal de erro salvo em erro_Q1_C.pcm\n");
    return 0;
}
