from scapy.all import sniff

def packet_callback(packet):
    print(f"Pacote capturado: {packet.summary()}")
    
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst
        protocol = packet['IP'].proto
        length = len(packet)

        print(f"\n** Informações do Pacote **")
        print(f"IP de origem: {ip_src}")
        print(f"IP de destino: {ip_dst}")
        print(f"Protocolo: {protocol}")
        print(f"Tamanho do pacote: {length} bytes")
        
        if packet.haslayer('TCP') and (packet['TCP'].dport == 80 or packet['TCP'].dport == 443):
            print(f"Este pacote é um pedido HTTP ou HTTPS.")
            print("HTTP é o protocolo usado para carregar páginas da web.")
            print("HTTPS é a versão segura do HTTP, que criptografa os dados transmitidos.")
        print("-" * 40)

def main():
    print("Iniciando a captura de pacotes...")
    print("Aperte Ctrl+C para parar a captura a qualquer momento.")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()