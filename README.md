# Projeto Dino - Bernardo Mello Correia Lima

Esse projeto foi criado com o propósito de criar uma inteligência artificial para o jogo do Google o qual um dinossauro deve correr enquanto desviando de cactus e pterodatilos.
O projeto foi feito como atividade pontuada para a matéria de Tópicos Avançados de Inteligência Artificial.

# Algoritimos Escolhidos

- Para a execução do projeto, foi escolhido a técnica de Multi-Layer-Perceptron, utilizando os parâmetros de distância, velocidade e altura adquirido pelo comando get_state() para alimentar as camadas da rede neural. O código para o perceptron está sendo usado da seguinte maneira:

![image](https://github.com/user-attachments/assets/a45489b6-e858-4f49-a653-a92e66895785)

```python
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init -)"' >> ~/.profile
exit
```
