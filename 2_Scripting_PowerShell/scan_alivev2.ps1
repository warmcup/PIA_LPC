$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "== Determinando gateway de la subred ..."
Write-Host "Gateway: $subred"
$rango = $subred.Substring(0, $subred.LastIndexOf('.') + 1)
Write-Host "== Determinando rango de subred ..."
Write-Host "Rango: $rango"
$rango_ip = @(1..254)
Write-Output ""
Write-Host "--Subred actual:"
Write-Host "Escaneando: " -NoNewline; Write-Host $rango -NoNewline; Write-Host "0/24" -ForegroundColor Red
Write-Output ""
foreach ($r in $rango_ip){
    $actual = $rango + $r
    $responde = Test-Connection $actual -Quiet -Count 1
    if ($responde){
        Write-Output ""
        Write-Host "Host responde: " -NoNewline; Write-Host $actual -ForegroundColor Green

    }
}