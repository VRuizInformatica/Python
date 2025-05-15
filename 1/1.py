# KeepAwake.ps1  ─ mueve el ratón 1 px cada 4 min
Add-Type -AssemblyName System.Windows.Forms
while ($true) {
    $pos = [System.Windows.Forms.Cursor]::Position
    [System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($pos.X + 1, $pos.Y)
    Start-Sleep -Milliseconds 50
    [System.Windows.Forms.Cursor]::Position = $pos        # vuelve al punto original
    Start-Sleep -Seconds 240                               # 4 min
}
