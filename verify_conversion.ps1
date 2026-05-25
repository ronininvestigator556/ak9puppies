$base = 'C:\Users\muram\Dev\ak9puppies\public\assets\processed'

# Check puppy subdirs
$puppyBase = Join-Path $base 'puppies'
Get-ChildItem $puppyBase -Directory | Sort-Object Name | ForEach-Object {
    $webp = (Get-ChildItem $_.FullName -Filter '*.webp').Count
    $orig = (Get-ChildItem $_.FullName -File | Where-Object { $_.Extension -ne '.webp' -and $_.Name -ne '.gitkeep' }).Count
    Write-Host ("  " + $_.Name.PadRight(12) + " webp: $webp  originals_left: $orig")
}

# Sample a few names from aang
Write-Host ""
Write-Host "Sample - aang:"
Get-ChildItem (Join-Path $puppyBase 'aang') -Filter '*.webp' | Select-Object -First 8 | ForEach-Object { Write-Host ("  " + $_.Name) }

Write-Host ""
Write-Host "Sample - parents:"
Get-ChildItem (Join-Path $base 'parents') -Filter '*.webp' | Select-Object -First 6 | ForEach-Object { Write-Host ("  " + $_.Name) }
