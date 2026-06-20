import geopandas as gpd
from shapely.geometry import Point

point = Point(77.2090, 28.6139)

gdf = gpd.GeoDataFrame(
    {"Location": ["Delhi"]},
    geometry=[point],
    crs="EPSG:4326"
)

gdf_projected = gdf.to_crs("EPSG:3857")

buffer = gdf_projected.buffer(1000)

buffer_gdf = gpd.GeoDataFrame(
    geometry=buffer,
    crs="EPSG:3857"
)

buffer_gdf.to_file("delhi_buffer.geojson", driver="GeoJSON")

print("Buffer created successfully!")
