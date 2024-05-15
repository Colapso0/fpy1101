import os
import time
clean='cls'
os.system(clean)
R=True
cnt_kil=0
cam=0
total=0
cam_kil=0
print("\nBienvenido a nuestra distribuidora de gas")
while(True):
    try:
        nom=str(input("Ingrese su nombre: "))
        if len(nom)>=1 and len(nom)>=3:
            print()
        else:
            print("Ingrese almenos 3 letras")
            continue
        Tel=int(input("Ingrese su nº de contacto: "))
        
        if len(str(Tel))<=9 and len(str(Tel))>=8:
            print()
        else:
            print("Ingrese entre 8 y 9 digitos")
            continue  
    except ValueError:
        print("Ingrese un valor valido")
        continue

    while(True):
        try:
            print("Limite maximo de kilos por camion= 450 kilos", "La entrega estandar se distribuye en cilindros de:", "5 Kilos=12 - 15 Kilos=20 - 45 Kilos=2", sep="\n")
            print("\n1. Compra entrega Camión estándar", )
            print("2. Compra entrega Carga específica")
            print("3. Imprimir boleta y cerrar pedido")
            compra=int(input(""))
            if compra==1:
                cnt_cam=int(input("Ingrese la cantidad de camiones: "))
                continue
            elif compra==2:
                while(R==True):
                    print("\n Indique la cantidad de cilindros")
                    print("1. 5 kilos")
                    print("2. 15 kilos")
                    print("3. 45 kilos")
                    print("4. Salir")
                    cil=int(input(""))
                    if cil==1:
                        cnt=int(input("Indique la cantidad de cilindros: "))
                        cnt_kil+=5*cnt
                    elif cil==2:
                        cnt=int(input("Indique la cantidad de cilindros: "))
                        cnt_kil+=15*cnt
                    elif cil==3:
                        cnt=int(input("Indique la cantidad de cilindros: "))
                        cnt_kil+=45*cnt
                    elif cil==4:
                        time.sleep(1)
                        break
                    else:
                        print("Ingrese una opcion valida")
            elif compra==3:
                if cnt_kil==0 and cnt_cam==0: 
                    print("ERROR", "NO PUEDES IMPRIMIR BOLETA EN 0", sep="\n")
                    continue
                os.system(clean)
                time.sleep(1)
                cam=cnt_cam
                total=cnt_cam*765000
                if cnt_kil>450:
                    cam_kil=(cnt_kil-450)/450
                    if type(cam_kil)==float:
                        cam_kil*450
                        cam_kil=cnt_kil//450
                        cam_kil+=2
                        cnt_kil=cnt_kil-450
                        total=(cnt_kil*1700+100000)+(cam*765000)
                    else:
                        cam_kil+=1
                        total=(cam_kil*765000)+(cam*765000)
                else:
                    cam=1+cnt_cam
                    total=(cnt_kil*1700+100000)+(cam*765000)
            

                print("\n", "_"*36)
                print(f'\tCliente: "{nom}"')
                print(f"\tTelefono: {Tel}")
                print(f"\tCamiones: {cam}")
                print(f"\tValor Total: {total}")



            else:
                print("Ingrese una opcion valida entre 1-3")
                continue
        except ValueError:
            print("ingrese un valor valido")
            continue
            
        print("¿Desea hacer otra cotizacion?(si/no)")
        t=input("")
        if t=="si":
            continue
        else:
            break
