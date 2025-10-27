### Introdução
O guia a seguir detalha o formato aceito pelo NADIA para a construção de provas de Dedução Natural em Lógica Proposicional e Lógica de Primeira Ordem no estilo Fitch:
**Importante:**
 - Os átomos e os predicados são escritos em letras maiúsculas (e.g. `A`, `B`, `H(x)`).
 - As variáveis são escritas com a primeira letra em minúsculo, podendo ser seguida de letras e números (e.g. `x`, `x0`, `xP0`).
 - Os símbolos de ⊥,⊢ e os conectivos ¬,∧,∨,→ são escritos por `@`,`|-`,`~`, `&`, `|`, `->` respectivamente.
 - As fórmulas com o ∀x e ∃x serão representadas por `Ax` e `Ex` (`A` e `E` seguidos da variável `x`). Por exemplo, `Ax (H(x)->M(x))` representa ∀x (H(x)→M(x)).
 - A ordem de precedência dos quantificadores e dos conectivos lógicos é definida por ¬,∀,∃,∧,∨,→ com alinhamento à direita. Por exemplo:
     - A fórmula `~A&B->C` representa a fórmula (((¬A)∧B)→C).
     - O teorema `~Ax P(x) |- Ex ~P(x)` representa o teorema (¬((∀x) P(x)))⊢((∃x) (¬P(x))).
 - As palavras _Premissa_ e _Hipótese_ são representadas por `pre` e `hip`, respectivamente.
Dedução Natural no Estilo de Fitch

O sistema de Dedução Natural é um mecanismo que permite a construção de uma prova formal, estabelecendo uma conclusão $\varphi$ a partir de um conjunto de premissas $\Gamma = \{\varphi_1, \varphi_2, \cdots, \varphi_n \}$, denotado por $\Gamma\vdash\varphi$, aplicando-se sucessivamente **regras de demonstração**.
Em Dedução Natural no estilo de Fitch, as demonstrações são apresentadas de forma linear e sequencial, na qual cada uma das linhas da prova é numerada, tem uma afirmação e uma justificativa. As justificativas são definidas por serem *premissas* da prova ou pela aplicação de uma das *regras do sistema dedutível*. As subprovas dentro de uma prova maior têm *caixas* ao redor e servem para delimitar o escopo de hipóteses temporárias. Provas podem ter caixas dentro de caixas, ou pode-se abrir outras caixas depois de fechar outras, obedecendo as regras de demonstração. Uma fórmula só pode ser utilizada em uma prova em um determinado ponto se essa fórmula aconteceu anteriormente e se nenhuma caixa que contenha essa ocorrência da fórmula tenha sido fechada.

A seguir iremos apresentar todas as regras do sistema de Dedução Natural no Estilo de Fitch.
***
### Explicar cada regra:
### Regra das Premissas

O primeiro passo em uma demonstração em Dedução Natural no estilo *Fitch* é enumerar as premissas da prova. Abaixo exibe-se a estrutura geral da regra das premissas, na qual $X1,X2,\ldots,Xn$ são representadas em uma linha cada, seguindo uma numeração sequencial e como justificativa "premissa" (pre).

***
```
1. X1  pre  
2. X2  pre  
⋮  
n. Xn  pre  
⋮  
```
 
***

### Regras da Conjunção

A regra da introdução da conjunção (&i) permite concluir a fórmula A&B em uma linha p se A e B foram demonstradas nas linhas m (ou n) e n (ou m), respectivamente, anteriores a linha p e que não foram descartadas. Abaixo exibe-se a aplicação &i da fórmula A&B na linha 3 a partir das fórmulas A e B, definidas nas linhas 1 e 2, respectivamente, que são anteriores a linha 3. 
##### NADIA - Exemplo: A,B|-A&B
***
```
1. A     pre
2. B     pre
3. A&B   &i 1,2
```
***
A regra da **eliminação da conjunção (&e)** permite concluir a fórmula A (ou B) na linha m a partir da eliminação à esquerda (ou à direita) da conjunção da fórmula A&B da linha n (anterior a p e não foi descartada). Abaixo exibe-se uma aplicação da regra na qual A é obtida na linha 3 pela eliminação da conjunção à esquerda da fórmula A&B da linha 1.
##### NADIA - Exemplo: A&B,C|-A&C
***
```
1. A&B    pre
2. C      pre
3. A      &e 1
4. A&C    &i 3,2
```
***
### Regras da Implicação

A regra da **eliminação da implicação (->e)**, também conhecida como _Modus Ponens_, permite concluir a fórmula B na linha p a partir da eliminação da implicação da fórmula A->B da linha m (ou n) e A da linha n (ou m), anteriores a p e não descartadas. Abaixo exibe-se uma aplicação da regra na qual a fórmula C é obtida na linha 4 pela eliminação da implicação das fórmulas B e B->C das linha 3 e 2, respectivamente.
##### NADIA - Exemplo: A&B,B->C|-C
***
```
1. A&B    pre
2. B->C   pre
3. B      &e 1
4. C      ->e 3,2
```
***
A regra da **introdução da implicação (->i)** constrói condicionais que não ocorrem como premissas. Para construção de um condicional é necessário realizar _raciocínio hipotético_, isto é, supor _temporariamente_ que uma dada fórmula é verdadeira. Chamamos esta fórmula de _hipótese_. Assim, utilizamos _caixas de demonstração_, que servem para delimitar o _escopo da hipótese temporária_. Nesta regra, para provar o condicional A->C na linha n+1, colocamos A como **hipótese** no topo de uma caixa (linha m), aplicamos um número finito de regras de forma a obter C na linha n. Todo o raciocínio para obter C depende da veracidade de A e, por isso, as fórmulas resultante deste raciocínio ficam delimitadas na caixa. Na linha seguinte (n+1) podemos aplicar a regra ->i para obter A→C, sendo que este condicional não mais depende da hipótese A. Na justificativa da linha n+1 utilizamos o nome da regra seguido das linhas inicial e final da caixa (->i m-n). Abaixo exibe-se uma aplicação da regra na qual a fórmula A->C é obtida na linha 6 a partir da caixa das linhas 3 a 5 em que A é a hipótese.
Observe que para a obtenção de C é possível utilizar quaisquer outras fórmulas como premissas e conclusões provisórias feitas até então. Demonstrações podem ter caixas dentro de caixas, ou pode-se abrir novas caixas depois de fechar outras. No entanto, existem regras sobre quais fórmulas podem ser utilizadas em que ponto na demonstração. Em geral, só podemos usar uma fórmula em um determinado ponto se esta fórmula ocorre _antes_ desse ponto e se nenhuma caixa que contenha a ocorrência desta fórmula tenha sido fechada.
##### NADIA - Exemplo: A->B,B->C|-A->C
***
```
1. A->B      pre
2. B->C      pre
3. {   A     hip
4.     B     ->e 3,1
5.     C     ->e 4,2
   }
6. A->C      ->i 3-5
```
***
### Regras da Disjunção

A regra da **introdução da disjunção (|i)** permite concluir a fórmula A|B em uma linha p se A (ou B) ocorre em uma linha m anterior a p e que não foi descartada. Abaixo exibe-se a aplicação da introdução da disjunção na linha 3 com a introdução de A|B a partir da fórmula A definida na linha 2.
##### NADIA - Exemplo: (A∨B)→C⊢A→C
***
```
1. (A|B)->C      pre
2. {   A         hip
3.     A|B       |i 2
4.     C         ->e 3,1
   }
5. A->C          ->i 2-4
```
***
A regra da **disjunção eliminação (|e)**, permite concluir uma fórmula X na linha p+1 se eliminarmos a disjunção da fórmula A|B na linha m e se fizermos a suposição de A em uma caixa, na linha m, e a suposição de B em outra caixa, na linha n+1, tal que ambas as caixas tenham como conclusão X, nas linhas n e p, respectivamente, por meio de uma sequência finita de passos (regras). Note que essa regra se assemelha a introdução da implicação no sentido de que fazemos raciocínio hipotético, nas caixas de (m+1)−n e (n+1)−p. Abaixo exibe-se a aplicação da eliminação da disjunção na linha 8, na qual concluímos C, a partir da disjunção de A|B na linha 3 e das caixas 4−5 e 6−7 onde supomos A na linha 4 e concluímos C na linha 5 e supomos B na linha 6 e concluímos C na linha 7.
##### NADIA - Exemplo: A->C,B->C,(A|B)|-C
***
```
1. A->C       pre
2. B->C       pre
3. A|B        pre
4. {   A      hip
5.     C      ->e 4,1
   }
6. {   B      hip
7.     C      ->e 6,2
   }
8. C          |e 3, 4-5, 6-7
```
***
### Regras da Negação

A regra da **negação eliminação (~e)** envolve a noção de **contradição**. Contradições são expressões da forma X&~X ou ~X∧X onde X é qualquer fórmula da lógica proposicional. A fórmula @ é utilizada para denotar uma contradição e este fato é expresso na regra ~e. Nesta regra temos que uma fórmula A na linha m (ou n) e a sua negação ¬A na linha n (ou m) podem ser combinadas para aparecimento da contradição @ na linha p com a aplicação da regra ~e. Abaixo exibe-se uma aplicação da regra na qual a contradição @ é obtida na linha 3 devido às fórmulas A na linha 1 e ¬A na linha 2.
##### NADIA - Exemplo: A,¬A⊢⊥
***
```
1. A     pre
2. ~A    pre
3. @     ~e 1,2
```
***
A regra da **negação introdução (¬i)**, é uma regra que envolve raciocínio hipotético e contradição. Se tomarmos A como hipótese (linha m) e, após a aplicação de um número finito de regras, chegarmos a uma contradição @ na linha n, significa que a hipótese não pode ser verdadeira. Desse modo, finalizamos nosso raciocínio hipotético introduzindo a negação na hipótese e obtendo ~A na linha n+1. Abaixo exibe-se um exemplo da aplicação da regra ~i, para provamos ~A na linha 6, assumimos A como hipótese no topo da caixa na linha 3 e chegamos a uma contradição no final da caixa na linha 5.
##### NADIA - Exemplo: A->B,~B|-~A
***
```
1. A->B      pre
2. ~B        pre
3. {   A     hip
4.     B     ->e 1,3
5.     @     ~e 2,4
   }
6. ~A        ~i 3-5
```
***
### Regra da Contradição

A **regra da contradição eliminação** permite concluir uma fórmula qualquer B na linha n se demonstramos em uma linha m, anterior a n, a contradição. Abaixo exibe-se a demonstração de B na linha 4 a partir da eliminação da contradição @ da linha 3.
##### NADIA - Exemplo: |- A->(~A->B)
***
```
1. {   A         hip
2.     {   ~A    hip
3.         @     ~e 1,2
4.         B     @e 3
       }
5.     ~A->B     ->i 2-4
   }
6. A->(~A->B)    ->i 1-5
```
***
### Regra de Redução ao Absurdo

A regra de **redução ao absurdo** é uma regra na qual para provarmos uma fórmula X em uma linha n+1, iremos supor temporariamente a negação da fórmula, ~X, em uma caixa que inicia na linha m e que conclui a contradição, @, na linha n, após uma sequência de aplicações de regras. Abaixo exibe-se a demonstração de A|~A, também conhecido como terceiro-excluído. Para provarmos A|~A na linha 8, fazemos a suposição de ~(A|~A), na linha 1 (início da caixa) e concluímos a contradição @, na linha 7 (fim da caixa).
### NADIA - Exemplo: ⊢A∨¬A
***
```
1. {   ~(A|~A)     hip
2.     {   ~A      hip
3.         A|~A    |i 2
4.         @       ~e 3,1
       }
5.     A           raa 2-4
6.     A|~A        |i 5
7.     @           ~e 6,1
   }
8. A|~A          raa 1-7
```
***
### Regra do Copie

A regra do **copie**, apresentada, é necessária, no estilo de Fitch, para permitir concluir uma caixa com uma fórmula que já apareceu anteriormente na demonstração. Abaixo exibe-se que, para demonstrar A->B, na linha 10, é preciso que a caixa que justifica a introdução da implicação inicie com A, linha 8, e termine com B, linha 9. Ocorre que a justificativa de B já havia sido realizada e, portanto, a justificativa da linha 9 é a cópia da fórmula da linhas 7.
##### NADIA - Exemplo: ~A|B ⊢A->B
***
```
1. ~A|B      pre
2. { ~A      hip
3.   { A     hip
4.     @     ~e 2,3
5.     B     @e 4
      }
6.   A->B    ->i 3-5
    }
7. { B       hip
8.   { A     hip
9.     B     copie 7
      }
10.  A -> B  ->i 8-9
    }
11. A -> B |e 1,2-6,7-10
```
***
### Regras do Universal

A regra da **eliminação do universal (Ae)** permite concluir a fórmula Fxt em uma linha p se ∀xF foi demonstrada na linha m, desde que o termo t seja substituível para a variável x em F. Abaixo exibe-se a aplicação de Ae da fórmula H(s) ->M(s) na linha 3 a partir da fórmula Ax(H(x)->M(x)), definida na linha 1.

##### NADIA - Exemplo: Ax(H(x)->M(x)),H(s)|-M(s)
***
```
1. Ax(H(x)->M(x))   pre
2. H(s)             pre
3. H(s)->M(s)       Ae 1
4. M(s)             ->e 2,3
```
***
A regra da **introdução do universal (Ai)**, é a regra na qual para provarmos AxF na linha n+1, iremos supor que para uma variável "a" qualquer (arbitrária) em uma caixa que inicia na linha m e que conclui Fxa, na linha n. Dizemos que a variável "a" é qualquer se ela é uma variável nova na linha m, ou seja, a não ocorre como variável livre de qualquer fórmula que aconteça anteriormente a linha m que não esteja em uma caixa fechada. Abaixo exibe-se a introdução do universal na linha 7 para provar AxM(x) a partir da suposição de a, no início da caixa, na linha 3, e demonstramos M(a) ao final da caixa, na linha 6. Note que a variável a escolhida não é uma variável livre das fórmulas das linhas 1 e 2.
##### NADIA - Exemplo: Ax(H(x)->M(x)),AxH(x)|-∀xM(x)
***
```
1. Ax(H(x)->M(x))        pre
2. Ax H(x)               pre
3. { a
4.      H(a)->M(a)       Ae 1
5.      H(a)             Ae 2
6.      M(a)             ->e 4,5
   }
7. Ax M(x)               Ai 3-6
```
***
### Regras do Existencial

A regra da **introdução do existencial (Ei)**, é a regra na qual a fórmula ExF pode ser concluída em uma linha p se Fxt foi demonstrada na linha m, desde que o termo t seja substituível para a variável x em F. Abaixo exibe-se a aplicação Ei da fórmula ExP(x) na linha 3 a partir da fórmula P(a), definida na linha 1.
##### NADIA - Exemplo: P(a),ExP(x)->B|-B
***
```
1. P(a)              pre
2. Ex P(x) -> B      pre
3. Ex P(x)           Ei 1
4. B                 ->e 3,2
```
***
A regra da **eliminação do existencial (Ee)**, é a regra na qual para provarmos uma fórmula α, na linha p+1, iremos eliminar o existencial da fórmula ExF, na linha m, supondo a fórmula Fxa para alguma variável a em uma caixa que inicia na linha n e que concluiu com uma fórmula α ao final da caixa, na linha p, desde que "a" não ocorra na conclusão α. Nesta regra sabemos que a fórmula F vale para algum elemento. Entretanto, não podemos assumir nenhuma propriedade específica para esta variável. Assim, a variável a deve ser uma variável nova na linha n, ou seja, a não ocorre como variável livre de qualquer fórmula que aconteça anteriormente a linha n que não esteja em uma caixa fechada e nem pode estar na conclusão α da regra.  
Abaixo exibe-se a eliminação do existencial para concluir @ na linha 9, a partir da fórmula ExH(x), na linha 3, e pela caixa que inicia na linha 4 com a suposição da fórmula H(a) com a (nova) variável a e que termina a caixa na linha 8 com a conclusão @.
##### NADIA - Exemplo: Ax(H(x)->M(x)),Ax~M(x)|-~AxH(x)
***
```
1. Ax(H(x)->M(x))         pre
2. Ax ~M(x)               pre
3. {  Ex H(x)             hip
4.    { a   H(a)          hip
5.          H(a)->M(a)    Ae 1
6.          M(a)          ->e 4,5
7.          ~M(a)         Ae 2
8.          @             ~e 6,7
      }
9.    @                   Ee 3, 4-8
   }
10.~Ex H(x)              ~i 3-9
```
***

### Erros nas Regras do Universal e do Existencial

Importante ressaltar que as restrições impostas as regras da introdução do universal e da eliminação do existencial são fundamentais para que todas as demonstrações sejam corretas. Na sequência, iremos apresentar alguns exemplos de demonstrações incorretas que não observam as restrições podem nos conduzir a conclusões erradas a partir de um conjunto de premissas. Os exemplos serão definidos no NADIA e os respectivos erros serão apontados pela ferramenta.
##### NADIA - Exemplo de Demonstração incorreta: P(a)|-AxP(x)
**Erro:** Na introdução do universal, a variável escolhida não pode ocorrer anteriormente.
***
```
1. P(a)           pre
2. { a
3.      P(a)      copie 1
   }
4. Ax P(x)        Ai 2-3
```
***
##### NADIA - Exemplo de Demonstração incorreta: ExP(x)|-P(a)
**Erro:** Na conclusão da eliminação do existencial, a variável escolhida na eliminação não pode ocorrer.
***
```
1. Ex P(x)   pre
2. { a  P(a) hip
   }
3. P(a)      Ee 1, 2-2
```
***
##### NADIA - Exemplo de Demonstração incorreta: Ex Par(x),Ex Impar(x)|-Ex(Par(x)&Impar(x))
**Erro:** Na eliminação do existencial, a variável escolhida na eliminação já ocorria anteriormente.
***
```
1. Ex PAR(x)                        pre
2. Ex IMPAR(x)                      pre
3. { a  PAR(a)                      hip
4.      { a   IMPAR(a)              hip
5.            PAR(a)&IMPAR(a)       &i 3,4
6.            Ex(PAR(x)&IMPAR(x))   Ei 5
        }
7.      Ex(PAR(x)&IMPAR(x))         Ee 2, 4-6
   }
8. Ex (PAR(x)&IMPAR(x))             Ee 1, 3-7
```
***
##### NADIA - Exemplo de Demonstração incorreta: AyEx MENOR(y,x)|-Ex MENOR(x,x)
**Erro:** Na eliminação do existencial, a variável escolhida na eliminação já ocorria anteriormente.
***
```
1. Ay Ex MENOR(y,x)       pre
2. Ex MENOR(a,x)          Ae 1
3. { a  MENOR(a,a)        hip
4.      Ex MENOR(x,x)     Ei 3
   }
5. Ex MENOR(x,x)          Ee 2, 3-4
```
***
