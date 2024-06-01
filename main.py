import trimesh
import numpy as np
import cv2

def obj_to_2d_projection(obj_path):
    mesh = trimesh.load(obj_path)

    vertices = mesh.vertices                # Get the 3D vertices and faces from the mesh
    faces = mesh.faces

    vertices_2d = vertices[:, :2]                # Project the 3D vertices onto a 2D plane (e.g., the XY plane)
    min_vals = np.min(vertices_2d, axis=0)            # Normalize vertices for better visualization
    max_vals = np.max(vertices_2d, axis=0)
    vertices_2d = (vertices_2d - min_vals) / (max_vals - min_vals) * 1000  # Scale to 1000x1000 image

    canvas_size = (1000, 1000)
    canvas = np.zeros(canvas_size, dtype=np.uint8)

    for face in faces:
        pts = vertices_2d[face].astype(np.int32)
        for i in range(len(pts)):
            cv2.line(canvas, tuple(pts[i]), tuple(pts[(i + 1) % len(pts)]), 255, 1)

    return canvas

def create_floor_plan(obj_path, output_path):
    canvas = obj_to_2d_projection(obj_path)

    edges = cv2.Canny(canvas, 50, 150)        # edge detection
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    floor_plan = np.zeros_like(canvas)
    cv2.drawContours(floor_plan, contours, -1, 255, 2)
    cv2.imwrite(output_path, floor_plan)

    cv2.imshow('Floor Plan', floor_plan)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

obj_path = input("Enter the path of the input file: ")
output_path = input("Enter the path of the output file: ")
create_floor_plan(obj_path, output_path)
