import numpy as np
import sys
import tiledb

# Name of the array to create.
array_name = "quickstart_dense"

def create_array():
    # Create a TileDB context
    ctx = tiledb.Ctx()

    # Check if the array already exists.
    if tiledb.object_type(ctx, array_name) == "array":
        print("Array already exists.")
        sys.exit(0)

    # The array will be 4x4 with dimensions "rows" and "cols", with domain [1,4].
    dom = tiledb.Domain(ctx,
                        tiledb.Dim(ctx, name="rows", domain=(1, 4), tile=4, dtype=np.int32),
                        tiledb.Dim(ctx, name="cols", domain=(1, 4), tile=4, dtype=np.int32))

    # The array will be dense with a single attribute "a" so each (i,j) cell can store an integer.
    schema = tiledb.ArraySchema(ctx, domain=dom, sparse=False,
                                attrs=[tiledb.Attr(ctx, name="a", dtype=np.int32)])

    # Create the (empty) array on disk.
    tiledb.DenseArray.create(array_name, schema)

create_array()