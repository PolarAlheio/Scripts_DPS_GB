import cv2
import sys
import os
import time

DELAY_S = 10

def main():
    # Cria pasta "fotos" se não existir
    #pasta = "fotos"
    #os.makedirs(pasta, exist_ok=True)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Erro ao abrir a câmera.")
        sys.exit(1)

    print("📷 Pressione 'p' para tirar foto.")
    print("🛑 Pressione ESC para sair.")
    print("⛔ Ctrl+C também encerra com segurança.")
    
    foto_count = 1
    max_fotos = 20

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("❌ Falha ao ler frame da câmera.")
                break

            cv2.imshow("Camera", frame)

            key = cv2.waitKey(1) & 0xFF

            # ESC -> sair
            if key == 27:
                print("🛑 ESC pressionado. Encerrando...")
                break

            # "p" -> tirar foto
            if key == ord('p'):
                time.sleep(DELAY_S)
                ret, frame = cap.read()
                if foto_count <= max_fotos:
                    filename = os.path.join(f"foto_{foto_count:02d}.jpg")
                    cv2.imwrite(filename, frame)
                    print(f"📸 Foto salva: {filename}")
                    foto_count += 1
                else:
                    print("✔️ Limite de 20 fotos atingido.")
                    break
            
            # Se tirou as 20 fotos, encerra automaticamente
            if foto_count > max_fotos:
                print("📁 Todas as fotos tiradas. Encerrando...")
                break

    except KeyboardInterrupt:
        print("\n🛑 Interrupção do teclado (Ctrl+C). Saindo com segurança...")

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("👋 Recursos liberados.")

if __name__ == "__main__":
    main()
