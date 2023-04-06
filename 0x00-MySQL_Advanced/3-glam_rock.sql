-- calculate lifesapn and rank
-- use split and formed to get lifespan
SELECT band_name, (split - formed) as lifespan
FROM metal_bands
WHERE style = "Glam rock"
ORDER BY lifespan DESC;
