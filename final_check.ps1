$base = 'C:\Users\muram\Dev\ak9puppies\public\assets\processed'
$allWebp = Get-ChildItem $base -Filter '*.webp' -Recurse -File | Where-Object { $_.Name -ne '.gitkeep' }
$allOther = Get-ChildItem $base -Recurse -File | Where-Object { $_.Extension -ne '.webp' -and $_.Name -ne '.gitkeep' }
Write-Host "Total WebP files : $($allWebp.Count)"
Write-Host "Remaining originals: $($allOther.Count)"
if ($allOther.Count -gt 0) {
    Write-Host "Leftover files:"
    $allOther | ForEach-Object { Write-Host ("  " + $_.FullName) }
}
