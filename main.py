import nglview
with open('protein.pdb', 'r') as pdb_file:
    pdb_data = pdb_file.read()
    protein = nglview.Structure(pdb_data)

# Удаление ненужных атомов из view
protein.clear_representations()
protein.add_representation('cartoon', selection='protein and not water and not ion and not hetero')
protein.add_representation('ball+stick', selection='ligand')

# Визуализация 3D-структуры
protein.center_view()
protein.add_surface(opacity=0.3)
protein.add_ball_and_stick()