
sed -i "/pad $1 smd/a pad $2 smd rect (at $3 $4) (size $5 $6) (layers F.Cu F.Paste F.Mask))" $7.kicad_mod
