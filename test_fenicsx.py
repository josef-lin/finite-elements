import dolfinx
import ufl
from mpi4py import MPI

print("DOLFINx version:", dolfinx.__version__)
print("MPI processes:", MPI.COMM_WORLD.size)

mesh = dolfinx.mesh.create_unit_square(
    MPI.COMM_WORLD, 8, 8
)
print("Mesh created successfully:", mesh.topology.dim)