#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define ROWS 24
#define COLS 14
#define K 1
#define SIGMA 1.0
#define REPS 10000

double gaussian(int i,int j){
    double a=1.0/ (2.0*M_PI*SIGMA*SIGMA);
    double b=-((i*i) +(j*j))/( 2.0*SIGMA *SIGMA);
    return a*exp(b);
}

double now_seconds(void){
    struct timespec ts;
    timespec_get(&ts,TIME_UTC);
    return ts.tv_sec+ts.tv_nsec/1e9;
}

int main(){
    FILE *f=fopen("results/grid.csv","r");
    if(f==NULL){
        printf("failed to open results/grid.csv\n");
        return 1;
    }

    double z[ROWS][COLS];
    double out[ROWS][COLS];

    for(int i=0;i<ROWS;i++){
        for(int j=0;j<COLS;j++){
            if(fscanf(f,"%lf",&z[i][j])!=1){
                printf("error reading grid at %d %d\n",i,j);
                fclose(f);
                return 1;
            }
            fgetc(f);
        }
    }

    fclose(f);

    double start=now_seconds();
    for(int r=0;r<REPS;r++){
        for(int x=0;x<ROWS;x++){
            for(int y=0;y<COLS;y++){
                double sum=0.0;

                for(int i=-K;i<=K;i++){
                    for(int j=-K;j<=K;j++){
                        int nx=x+i;
                        int ny=y+j;

                        if(nx>=0&&nx<ROWS&&ny>=0&&ny<COLS){
                            sum+=z[nx][ny]*gaussian(i,j);
                        }
                    }
                }

                out[x][y]=sum;
            }
        }
    }
    double end=now_seconds();
    printf("time = %.6f seconds\n",end-start);

    printf("smoothing done\n");
    printf("out[0][0]=%.2f\n",out[0][0]);
    printf("out[0][1]=%.2f\n",out[0][1]);
    printf("out[1][0]=%.2f\n",out[1][0]);


    FILE *g=fopen("results/seq_output.csv","w");
    if(g==NULL){
        printf("failed to open seq_output.csv\n");
        return 1;
    }

    for(int i=0;i<ROWS;i++){
        for(int j=0;j<COLS;j++){
            fprintf(g,"%.6f",out[i][j]);
            if(j<COLS-1) fprintf(g,",");
        }
        fprintf(g,"\n");
    }

    fclose(g);

    printf("saved to results/seq_output.csv\n");
    return 0;
}
