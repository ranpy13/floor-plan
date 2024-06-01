import trimesh
import numpy as np
import cv2

def obj_to_2d_projection(obj_path):
    # Load the 3D .obj file
    mesh = trimesh.load(obj_path)

    # Get the 3D vertices and faces from the mesh
    vertices = mesh.vertices
    faces = mesh.faces

    # Project the 3D vertices onto a 2D plane (e.g., the XY plane)
    # Normalize vertices for better visualization
    vertices_2d = vertices[:, :2]
    min_vals = np.min(vertices_2d, axis=0)
    max_vals = np.max(vertices_2d, axis=0)
    vertices_2d = (vertices_2d - min_vals) / (max_vals - min_vals) * 1000  # Scale to 1000x1000 image

    # Create a blank canvas
    canvas_size = (1000, 1000)
    canvas = np.zeros(canvas_size, dtype=np.uint8)

    # Draw the edges of the 2D projection
    for face in faces:
        pts = vertices_2d[face].astype(np.int32)
        for i in range(len(pts)):
            cv2.line(canvas, tuple(pts[i]), tuple(pts[(i + 1) % len(pts)]), 255, 1)

    return canvas

def create_floor_plan(obj_path, output_path):
    # Get the 2D projection of the .obj file
    canvas = obj_to_2d_projection(obj_path)

    # Apply Canny edge detection
    edges = cv2.Canny(canvas, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Create a blank canvas to draw the floor plan
    floor_plan = np.zeros_like(canvas)

    # Draw the contours on the blank canvas
    cv2.drawContours(floor_plan, contours, -1, 255, 2)

    # Save the resulting floor plan
    cv2.imwrite(output_path, floor_plan)

    # Display the floor plan
    cv2.imshow('Floor Plan', floor_plan)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
obj_path = '/path/to/your/3d_model.obj'
output_path = '/path/to/save/floor_plan.jpg'
create_floor_plan(obj_path, output_path)
