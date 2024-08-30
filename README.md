# Network Packet Sniffer

Este script em Python utiliza a biblioteca Scapy para capturar e exibir informações detalhadas sobre pacotes de rede, incluindo endereços IP, protocolos, tamanho dos pacotes e se o tráfego corresponde a pedidos HTTP ou HTTPS.

## Descrição

O script captura pacotes de rede em tempo real e exibe informações relevantes, como:

- IP de origem e destino
- Protocolo utilizado
- Tamanho do pacote
- Identificação de tráfego HTTP ou HTTPS

Essas informações são úteis para monitorar e analisar o tráfego de rede, ajudando a entender os dados que estão sendo transmitidos e recebidos pelo sistema.

## Requisitos

- Python 3.12.5
- Biblioteca Scapy

Você pode instalar a Scapy utilizando o seguinte comando:

```
pip install scapy
```
## Como Usar
Clone o repositório ou copie o código para um arquivo Python.
Execute o script com privilégios administrativos para capturar pacotes de rede:
```
sudo python nome_do_arquivo.py
```
O script começará a capturar pacotes e exibir as informações no terminal. Para interromper a captura, pressione Ctrl + C.
Exemplo de Saída
```
Iniciando a captura de pacotes...
Aperte Ctrl+C para parar a captura a qualquer momento.
Pacote capturado: IP / TCP 192.168.1.2:58324 > 192.168.1.1:http S
** Informações do Pacote **
IP de origem: 192.168.1.2
IP de destino: 192.168.1.1
Protocolo: 6
Tamanho do pacote: 48 bytes
Este pacote é um pedido HTTP ou HTTPS.
HTTP é o protocolo usado para carregar páginas da web.
HTTPS é a versão segura do HTTP, que criptografa os dados transmitidos.
----------------------------------------
```
## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Autor
Lucas Rial
