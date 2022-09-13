'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

05/09/2022
===================================================='''

from re import S
from turtle import shape
import numpy as np

'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: matriz de adjacências (numpy.ndarray), vi (Integer), vj (Integer)
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''
def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0: # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes

'''Função para se obter o tipo do grafo a partir de sua matriz de adjacências.
Saída: 0 se o grafo for simples; 1 se for um digrafo; 2 se estiver lidando com um
multigrafo; 3 se a opção for um pseudografo '''
def tipoGrafo(matriz):
    tiposGrafos = {
    0:"Grafo_Simples",
    1:"Digrafo" ,
    2:"Multigrafo",
    3:"Pseudografo"
    }

    #Se nenhuma condição for alcançada o grafo, consequentimente, é simples
    tipoGrafo=0
    #Variaveis auxiliadoras para os indices da matriz
    valorX=0
    valorY=0
    for x in matriz:
        valorY=0
        for y in x:
            if(y>0):
                #Valores na celula maiores que 1 indicam um multigrafo ou pseudografo
                if(y>1):
                    tipoGrafo=2
                #Se não houver simetria na matriz o grafo é direcionado, ou seja, um digrafo
                if(matriz[valorY][valorX]!= y):
                    tipoGrafo=1
            
            #Valores na diagonal maiores que 0 indicam um pseudografo
            if(valorY==valorX):
                if(y>1):
                    tipoGrafo=3
            valorY+=1
        valorX+=1
        
    print("Este grafo é um " + tiposGrafos[tipoGrafo])
    return tipoGrafo

'''Função para o calculo da densidade de um grafo, retornando essa densidade com 
precisão de 3 casa decimais''' 
def calcDensidade(matriz):

    #Se nenhuma condição for alcançada o grafo, consequentimente, é simples
    tipoGrafo=0
    #Variaveis auxiliadoras para os indices da matriz
    valorX=0
    valorY=0
    #contador de arestas
    E=0
    for x in matriz:
        valorY=0
        for y in x:
            if(y>0):
                #Se não houver simetria na matriz o grafo é direcionado, ou seja, um digrafo
                if(matriz[valorY][valorX]!= y):
                    tipoGrafo=1
                #somando as arestas
                E+=y;    
            valorY+=1
        valorX+=1

    #quantidade de arestas
    E=E/2
    #quantidade de vertices
    V=np.shape(matriz)[0]
    

    #calculo densidade matriz não direcionada
    if tipoGrafo==0:
        D=(2*E)/(V*(V-1))
        #arredondando as casas decimais
        D = round(D, 3)
    
    #calculo densidade matriz direcionada
    else:
 
        D=E/(V*(V-1))
        #arredondando as casas decimais
        D = round(D, 3)
        

    print("\nA densidade desse grafo é de "+ str(D))    
    return D

'''Função para inserir uma aresta no grafo considerando as arestas Vi e Vj
passadas a função.
Vale ressaltar que a implementação segue o conceito de adicionar aresta inde-
pendente da pré existencia de arestas entre esses dois vertices, ou seja, podem
 haver multiplas arestas entre dois vertices'''
def insereAresta(matriz, Vi, Vj):
    #Necessario verificar se o grafo é direcionado para inserir corretamente a aresta
    tipoGrafo=0
    #Variaveis auxiliadoras para os indices da matriz
    valorX=0
    valorY=0
    for x in matriz:
        valorY=0
        for y in x:
            #Se não houver simetria na matriz o grafo é direcionado, ou seja, um digrafo
            if(matriz[valorY][valorX]!= y):
                tipoGrafo=1    
            valorY+=1
        valorX+=1
    matriz[Vi][Vj]+=1
    #mantendo matriz equilibrada no caso do grafo não ser direcionado
    if tipoGrafo==0:
        matriz[Vj][Vi]+=1

    print("Aresta entre os vertices "+ str(Vi)+" " +str(Vj) +" inserida do grafo")
    return matriz

'''Função para inserir um vertice no grafo considerando o id (Vi) do vertice
passado a função'''
def insereVertice(matriz, Vi):
    novaMatriz= np.resize (matriz, [Vi,Vi])
    for i in range(Vi):
        novaMatriz[Vi][i]=0
        novaMatriz[i][Vi]=0
    print("Novo vértice"+str(Vi)+ " foi adicionado ao grafo")
    return novaMatriz
 

    

'''Função para remover uma aresta do grafo considerando as arestas Vi e Vj passadas a função
Vale ressaltar que a implementação segue o conceito de remover uma aresta indenpedente da
circunstância, ou seja, é feita a remoção, mas podem haver outras arestas entre aqueles dois vertices'''
def removeAresta(matriz, Vi, Vj):
    #Necessario verificar se o grafo é direcionado para remover corretamente a aresta
    tipoGrafo=0
    #Variaveis auxiliadoras para os indices da matriz
    valorX=0
    valorY=0
    for x in matriz:
        valorY=0
        for y in x:
            #Se não houver simetria na matriz o grafo é direcionado, ou seja, um digrafo
            if(matriz[valorY][valorX]!= y):
                tipoGrafo=1    
            valorY+=1
        valorX+=1
    #Se na posição não houver valor,significa que não ha aresta entre esses dois vertices, 
    # então não é necessario fazer a remoção
    if(matriz[Vi][Vj]==0):
        pass
    else:
        matriz[Vi][Vj]-=1

    #mantendo matriz equilibrada no caso do grafo não ser direcionado
    if tipoGrafo==0:
        #Se na posição não houver valor,significa que não ha aresta entre esses dois vertices, 
        # então não é necessario fazer a remoção
        if(matriz[Vj][Vi]==0):
            pass
        else:
            matriz[Vj][Vi]-=1
    
    print("Aresta entre os vertices "+ str(Vi)+" " +str(Vj) +" removida do grafo")
    return matriz

'''Função para remover um ventice do grafo considerando o id (Vi) do vertice
passado a função'''
def removeVertice(matriz, Vi):
    #excluindo a linha e a coluna referente ao id(Vi) do vertice
    matrizNova =np.delete(matriz,(Vi), axis=0)
    matrizNova =np.delete(matrizNova,(Vi), axis=1)
    print("O vertice "+str(Vi)+ " foi removido do grafo")
    return matrizNova


