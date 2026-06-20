from pyproj import Transformer

lat = 28.6139
lon = 77.2090

transformer = Transformer.from_crs(
    "EPSG:4326",
    "EPSG:32643",
    always_xy=True
)

x, y = transformer.transform(lon, lat)

print(f"UTM Easting: {x:.2f}")
print(f"UTM Northing: {y:.2f}")
