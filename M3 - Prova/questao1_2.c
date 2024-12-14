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
    for (int n = M; n < N; n++) {
        y = 0.0;

        // Calcular a saída do filtro
        for (int k = 0; k < M; k++) {
            y += w[k] * x[n - k];
        }

        // Calcular o erro
        e[n] = d[n] - y;

        // Atualizar os coeficientes do filtro
        for (int k = 0; k < M; k++) {
            w[k] += 2 * u * e[n] * x[n - k];
        }
    }
}

int main() {
    // Parâmetros do LMS
    const int N = 40000; // Número de amostras (ajustar conforme necessário)
    const int M = 8;     // Tamanho do filtro adaptativo (baseado no teste de convergência)
    const float u = 0.05; // Passo de adaptação (baseado no teste de convergência)

    // Buffers para os sinais
    float *x = (float *)malloc(N * sizeof(float));
    float *d = (float *)malloc(N * sizeof(float));
    float *e = (float *)malloc(N * sizeof(float));
    float *w = (float *)calloc(M, sizeof(float)); // Inicializar os coeficientes do filtro com zeros

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
