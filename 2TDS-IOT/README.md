# Projeto IoT com ESP32 Simulado no Wokwi

![VSCode](https://img.shields.io/badge/Editor-VSCode-blue?logo=visualstudiocode)
![PlatformIO](https://img.shields.io/badge/Build-PlatformIO-orange?logo=platformio)
![Wokwi](https://img.shields.io/badge/Simulator-Wokwi-green?logo=cloud)

## Descrição  
Este projeto demonstra como configurar um **ESP32** no **Visual Studio Code** utilizando a extensão **PlatformIO**, em conjunto com o **Wokwi Simulator**.  
A simulação permite desenvolver e testar aplicações sem a necessidade de hardware físico.  

## Adaptação  
Este repositório é uma adaptação do seguinte tutorial: [link](https://docs.google.com/document/d/1y6IfbOT_rAimZx41tNBL9NlscoB1ObjgaPmy2g4UGO0/edit?usp=sharing)  

## Funcionalidades  
- **Configuração no VSCode**: Projeto estruturado com PlatformIO.  
- **Integração com Wokwi**: Simulação online do ESP32.  
- **Teste sem hardware físico**: Desenvolvimento totalmente em ambiente simulado.  

⚠️ **Importante**: Para usar o Wokwi integrado ao VSCode e ao PlatformIO, é necessário habilitar a **licença Wokwi Pro**.  

## Pré-requisitos  
- [Visual Studio Code](https://code.visualstudio.com/)  
- [PlatformIO IDE](https://platformio.org/install/ide?install=vscode)  
- Conta no [Wokwi](https://wokwi.com/) com licença habilitada  

## Instalação  

1. **Clone o repositório:**  
   ```bash
   https://github.com/prof-atritiack/2TDS-IOT
   ```  

2. **Abra no VSCode:**  
   Navegue até a pasta do projeto e abra no Visual Studio Code.  

3. **Dependências:**  
   O PlatformIO instalará automaticamente as bibliotecas necessárias na primeira compilação.  

## Uso  

1. **Compilação:**  
   No PlatformIO, clique em **Build** para compilar o código.  

2. **Simulação:**  
   - Inicie a simulação no Wokwi.  
   - Acompanhe os logs pelo monitor serial do VSCode.  

3. **Dicas de simulação:**  
   - O Wokwi simula em tempo real, mas a execução pode variar em desempenho.  
   - Utilize o monitor serial para acompanhar o comportamento do ESP32.  
