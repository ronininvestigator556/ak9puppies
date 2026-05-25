$base = 'C:\Users\muram\Dev\ak9puppies\public\assets\processed'
$dirs = Get-ChildItem $base -Directory | Sort-Object Name
foreach ($d in $dirs) {
    $webp = (Get-ChildItem $d.FullName -Filter '*.webp' -File).Count
    $other = (Get-ChildItem $d.FullName -File | Where-Object { $_.Extension -ne '.webp' -and $_.Name -ne '.gitkeep' }).Count
    Write-Host ($d.Name.PadRight(15) + " webp: $webp  remaining_originals: $other")
}
