comp_pista, dist_pedagios = map(int, input().split())
custo_km, custo_pedagio = map(int, input().split())
gasto1 = (comp_pista / dist_pedagios) * custo_pedagio
gasto2 = comp_pista * custo_km
print(int(gasto1 + gasto2))