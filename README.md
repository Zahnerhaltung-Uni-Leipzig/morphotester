# MorphoTester

## Version 1.2

**Original Author:** Julia Winchester (<julia.winchester@stonybrook.edu>)  
**Updated by:** [Tobias] ([GitHub Profile](https://github.com/T0bC))

---

> **Note:** This software has been updated from Python 2.x to Python 3.12, including necessary changes to the Qt framework and related dependencies. See [Changelog](#changelog) for details.

---

## Overview

![MorphoTester Interface](www/MorphoTester.png)

MorphoTester is a scientific computing application for quantifying topographic shape from three-dimensional triangulated meshes representing anatomical shape data. Shape is described via three metrics which characterize distinct aspects of form:

- **Curvature** – Dirichlet Normal Energy (Bunn et al., 2011; Winchester, in preparation)
- **Relief** – Relief Index (Ungar and M'Kirera, 2003; Boyer, 2008)
- **Complexity** – Orientation Patch Count Rotated (Evans et al., 2007; Winchester, in preparation)

Details on relevant methods can be found in the listed publications. This application provides a flexible engine for viewing 3D triangulated meshes and calculating topographic metrics from individual files or directory batches.

## Installation & Running

### Using Conda Environment

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/).

2. Create the environment from the provided `environment.yml`:

   ```bash
   conda env create -f environment.yml
   ```

3. Activate the environment:

   ```bash
   conda activate morphotester
   ```

4. Run the application:

   ```bash
   python Morpho.py
   ```

### Building a Standalone Executable

To create a standalone executable (`.exe` on Windows, `.app`/`.dmg` on macOS), use PyInstaller with the provided spec file:

1. Ensure the conda environment is activated and PyInstaller is installed (included in `environment.yml`, or install via `pip`).

2. Build the executable:

   ```bash
   pyinstaller Morpho.spec --clean
   ```

3. The resulting executable will be located in the `dist/` folder.

## File Type and Size

MorphoTester accepts `.ply` Stanford PLY format surface mesh files. Triangulated surface mesh files (surfaces comprised of multiple interconnected triangular polygons in three-dimensional space) can be generally described by the number of triangular polygons comprising each mesh.

**Performance considerations:**

- MorphoTester may be slow to load surface meshes consisting of >500,000 faces depending on computer speed
- DNE implicit fair mesh smoothing will be very slow at >20,000 triangles
- Previously published work using this software has analyzed surface meshes simplified to 10,000 faces

Applications capable of mesh simplification include Amira, Aviso, or the freeware application Meshlab. Future versions of MorphoTester may include mesh simplification built in.

## Processing Single Files

1. Load a single file by selecting **Open File**, navigating to the desired file, and selecting Open. The surface can be inspected using the 3D viewer on the right.

2. Choose which topographic metrics are to be measured. Set parameters and optional procedures for DNE and OPCR calculation using the nearby **Options** button (see DNE Options and OPCR Options below).

3. Select **Process File** and wait. Values will be output shortly.

## Batch Processing Multiple Files

1. All `.ply` meshes to be measured should be located in a single directory.

2. Select **Open Directory** and navigate to the desired directory for analysis. Select Open. No mesh will appear in the 3D viewer.

3. Choose which topographic metrics are to be measured, and use the Option menus to set parameters.

4. Select **Process Directory** and wait. Values will be output shortly. If an error occurs, this process will halt entirely.

Batch processing produces a results file in the directory where analyzed files are located. Results are provided as a tab-delineated table of topographic values and file names, and may be opened in Microsoft Excel or other applications.

## DNE Options

If optional model smoothing for DNE is desired, check **DNE Implicit Fairing Smooth**. All previously published DNE calculations employ this smoothing, with a smoothing iteration number of 3 and a step size of 0.1. This smoothing step can introduce possible application errors, but it can also help reduce surface mesh noise which can disproportionately affect DNE values. DNE can be calculated regardless of whether implicit fairing is enabled. If implicit fairing is not enabled, the iteration number and step size values are ignored.

Overall DNE can be disproportionately affected by intersections between polygons with extreme angles such as often results from mesh noise or erroneous sharp features on surface casts pre-scanning (see "Absurdly High DNE Values" below). To address this, the **Outlier Removal** option culls individual polygonal DNE values above a user-specified percentile amount. Outliers can be removed from the sample of energy quantities per polygon (energy density × polygon area) or raw energy densities. Outlier removal at 99.9th percentile using energy density × polygon area is currently recommended.

Similarly, the **Condition number checking** option removes individual polygon DNE values when the matrix comprising the face has a high condition number. High condition numbers can indicate a matrix is singular (meaning further calculation of DNE cannot continue) and/or that the particular polygonal intersection is unreliable as a shape indicator due to extreme changes in DNE from minor changes in polygon position. Condition number checking should generally be left on, unless specific reasons indicate turning it off.

If **Visualize DNE** is checked, energy quantity values will be visualized across a mesh surface as a heatmap. Relative DNE visualization uses minimum and maximum surface polygon energy quantities to bound the heatmap legend, and is useful for plotting DNE across an individual surface. Absolute DNE visualization allows the user to specify the bounds of the heatmap plotting and is useful for comparing DNE between two surfaces.

## OPCR Options

**Minimum Patch Count** defines the smallest size of a patch (in terms of number of triangles comprising the patch) which will be counted for OPC calculation (see Evans et al., 2007 for more detail). 3 is the default value.

If **Visualize OPCR** is checked, OPCR results for single files will be depicted as colored patches on the mesh surface in the 3D window viewer pane on the right. Patches are colored according to their aspect, with each of the eight colors representing an arc of 45 degrees. This visualization is similar to that provided by Evans et al. (2007), but differs in that it represents aspect-designated patches on a fully 3D mesh instead of a GIS grid of single Z escalation values associated with XY coordinate pairs.

## Changes from Beta Versions

### Different RFI Results

Compared to latest release versions, some older betas of MorphoTester generate different values for "outline area." Outline area is the 2D area of a 3D surface as projected onto the XY plane (for dental analyses this is often the occlusal plane). MorphoTester calculates 2D projected area by producing a flat pixelated image of a surface, counting surface pixels, and then multiplying this count by an area to pixel ratio. The pixel counting method used here was updated midway through beta development to ensure compatibility between Windows and OSX environments. Any differences in outline area should be small, usually around 1%.

### Different DNE Results with Outlier Removal

Unlike for RFI, the latest version of MorphoTester should be able to replicate all DNE results obtained from any beta version. The base DNE method is identical across all versions, but certain beta versions do use different protocols for removing outliers (polygons with extremely high energy values):

- Older beta versions removed polygons with energy values above the 99th percentile (for a mesh of 10,000 polygons, 100 outliers removed)
- Later beta versions changed this to only remove polygons with energy values above the 99.9th percentile (for a mesh of 10,000 polygons, 10 outliers removed)
- In both cases, outliers were removed from values calculated as energy density multiplied by polygon face area
- Beta version 0.2.0d removed outliers from values calculated as raw energy densities

The latest version of MorphoTester allows users to specify outlier percentile and whether outliers should be removed from energy densities × polygon areas or raw energy densities. Outlier removal at 99.9% using energy densities × polygon areas is currently recommended, but trends of differences between specimens should be generally similar regardless of approach.

## Known Issues

### Windows 8 64-bit Version

Due to slight instability in dependent packages in 64-bit Windows 8, this version of MorphoTester experiences two minor issues relating to mesh visualization:

- When visualizing meshes, a VTK/OpenGL error message will appear. Mesh visualization will occur normally despite this, and the error message can be closed without any consequences.
- When visualizing surface DNE, scale bars will often be placed partially off-screen. This can be largely fixed by running MorphoTester as an administrator. If scale bar misplacement occurs while running as administrator, reloading the surface should fix this.

All other features work appropriately.

### CHOL Errors

This is the primary issue likely to be encountered with MorphoTester. It will only be encountered when measuring DNE with implicit fairing smoothing. This error relates to the matrices that comprise the surface data, and in practice it has mostly been encountered as a result of smoothing operations completed by Amira or Aviso.

**Workaround:** If implicit fairing is desired (for comparability to current DNE results), do not use smoothing functions from Amira or Aviso. Meshlab works equally well for this purpose. For models already encountering this error, applying a 1 or 2-iteration Laplacian smooth using Meshlab will fix the problem while not affecting DNE values significantly.

### Absurdly High DNE Values

DNE can be sensitive to certain kinds of surface noise or mesh artifacts that are not biological, such as:

- Long thin gaps in surface models
- Triangular polygons overlapping one another or sitting at bizarre angles
- Accessory isolated polygon regions distinct from the surface to be analyzed

This is not an issue with MorphoTester, but instead requires care in preparing surface meshes to reduce noise or remove non-biological surface errors. In previously published DNE results, 100 iterations of smoothing has been used on simplified 10,000-face polygonal models for this purpose.

---

## Changelog

### Version 1.2

**Updated by:** [Tobias]

This version updates MorphoTester from Python 2.x to Python 3.12 with the following changes:

- **Python version upgrade:** Migrated from Python 2.x to Python 3.12
- **Qt framework update:** Updated from PyQt4 to PyQt5
- **Print statements:** Converted all `print` statements to `print()` function calls
- **Integer division:** Updated division operators where necessary (`/` to `//` for integer division)
- **String handling:** Updated string handling for Python 3 compatibility
- **Dependencies:** Updated all dependencies to Python 3 compatible versions (NumPy, SciPy, Matplotlib, Pillow, Traits, TraitsUI, Mayavi, VTK)
- **Environment file:** Added `environment.yml` for easy conda environment setup
- **Build configuration:** Added `Morpho.spec` PyInstaller spec file for building standalone executables
- **PLY file compatibility:** Fixed ASCII PLY loading to only read the first 3 vertex columns (x, y, z). PLY files with additional vertex properties (e.g., color, normals, alpha) are now supported — extra channels are automatically filtered out
