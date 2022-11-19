# Autor: Juan Angel Garza Castillo
# Matricula: 2007612

Clear-Host
Write-Host "Ejemplo de codificador Base64 en PowerShell" -ForegroundColor Yellow
$texto = 'TABhAGIAbwByAGEAdABvAHIAaQBvACAAZABlACAAUAByAG8AZwByAGEAbQBhAGMAaQDzAG4AIABwAGEAcgBhACAAQwBpAGIAZQByAFMAZQBnAHUAcgBpAGQAYQBkACAAUwBlAHMAaQDzAG4AIAAxADAA
'
Write-Host "La cadena a decodificar es:" $texto
$decoded = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String(($texto)))

Write-Host "La cadena ya decodificada es:" $decoded -ForegroundColor Green