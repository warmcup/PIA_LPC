$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "Gateway: $subred"
$rango = $subred.Substring(0, $subred.LastIndexOf('.') + 1)
Write-Host "Rango: $rango"
$rango_ip = @(1..254)
foreach ($r in $rango_ip){
    $actual = $rango + $r
    $responde = Test-Connection $actual -Quiet -Count 1
    if ($responde){
        Write-Output ""
        Write-Host "Host responde: " -NoNewline; Write-Host $actual -ForegroundColor Green

    }
}