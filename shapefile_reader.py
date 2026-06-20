import geopandas as gpd

shapefile = "sample_shapefile.shp"

gdf = gpd.read_file(shapefile)

print("Columns:")
print(gdf.columns)

print("\nCoordinate System:")
print(gdf.crs)

print("\nFirst Five Records:")
print(gdf.head())
