pro efs
smax=17
nr1=0l
nread=4644l
mesh=dblarr(2400)
cs=dblarr(50)
func=dblarr(2,2400)
ksir=dblarr(2400,nread)
etar=dblarr(2400,nread)
lmode=intarr(nread)
nmode=intarr(nread)
numode=dblarr(nread)
openr,1,'./dlfiles/WB-2.1_models_l5bi.d.15_amde.1',/f77_unformatted
readu,1,nr1,mesh
for nfunc=0,nread-1 do begin
  readu,1,cs,func
  l=nint_new(cs(17))
  n=nint_new(cs(18))
  nu=1000*cs(26)
; Already multiplied by sqrt(rho). Multiply by r and correct for JCD scaling.
  ksir(*,nfunc)=func(0,*)/sqrt(mesh)
  etar(*,nfunc)=func(1,*)/sqrt(mesh)
; Fix center
  ksir(0,nfunc)=0
  etar(0,nfunc)=0
  lmode(nfunc)=l
  nmode(nfunc)=n
  numode(nfunc)=nu
end
close,1

ksir_fname='./ksir.csv'
etar_fname='./etar.csv'
lmode_fname='./l.csv'
nmode_fname='./n.csv'
r_fname='./r.csv'
nu_fname='./muhz.csv'

write_csv, ksir_fname, ksir
write_csv, etar_fname, etar
write_csv, lmode_fname, lmode
write_csv, nmode_fname, nmode
write_csv, r_fname, mesh
write_csv, nu_fname, numode
end

