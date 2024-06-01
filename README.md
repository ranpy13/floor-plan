# floor-plan
> _Converts 3D images to floor plans using simple python tools, openCV and contour detection_
---

### Procedure

* Load the 3D `.obj` file: Use the `trimesh` library to load the 3D model.
* Project the 3D model onto a 2D plane: Convert the 3D vertices to 2D coordinates.
* Render the 2D projection: Create an image from the 2D projection.
* Edge detection: Use OpenCV's Canny edge detection.
* Find and draw contours: Use OpenCV's findContours and drawContours to create the floor plan.


### Explanation:

1. **Loading the 3D `.obj` file**: The `trimesh` library is used to load the 3D model and extract its vertices and faces.
2. **Projection to 2D**: The 3D vertices are projected onto the 2D plane by taking the XY coordinates. The vertices are normalized to fit into a 1000x1000 pixel image for better visualization.
3. **Drawing the 2D projection**: The edges of the 2D projection are drawn onto a blank canvas using OpenCV’s `line` function.
4. **Edge detection**: Canny edge detection is applied to the 2D projection.
5. **Finding and drawing contours**: The contours are found and drawn to create the floor plan. The resulting image is saved and displayed.

### Dependencies:
- `trimesh`: For loading and handling the 3D `.obj` file.
- `numpy`: For numerical operations.
- `opencv-python`: For image processing.

You can install the required libraries using pip:
```bash
pip install trimesh numpy opencv-python
```

### Next Steps:
**a.** Add additional preprocessing steps, like filtering out small contours, to improve the floor plan's accuracy.

**b.** Integrate a GUI to allow users to select the `.obj` file and visualize the floor plan interactively.
