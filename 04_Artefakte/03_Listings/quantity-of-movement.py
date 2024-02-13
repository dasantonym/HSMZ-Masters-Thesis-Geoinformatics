distance = pcd_data.compute_point_cloud_distance(self.last_pcd)
changed_indices = np.nonzero(np.asarray(distance, dtype=np.float64) > 0.01)
quantity_of_motion = len(changed_indices[0]) / len(dist_array)
