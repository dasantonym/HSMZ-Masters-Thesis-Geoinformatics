bounding_box = pcd_data.get_axis_aligned_bounding_box()
bounding_box_volume = bounding_box.volume()

convex_hull_mesh, index_list = pcd_data.compute_convex_hull()
surface_volume = convex_hull_mesh.get_volume()

contraction_index = surface_volume / bounding_box_volume
