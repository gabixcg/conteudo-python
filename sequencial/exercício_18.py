tah_arquivo = float(input("digite o tamanho do arquivo em MB"))
velo_link = float(input("digite a velocidade da internet em Mbps: "))

tmp_se = tah_arquivo / velo_link

tmo_minu = tmp_se / 60

print("tempo de download é em: ",round(tmo_minu,2),"minutos ou" ,round(tmp_se,2),"segundos!")
