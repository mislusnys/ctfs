import java.math.BigInteger;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;
import java.util.TreeMap;
import java.util.Vector;
 
 
public class Test1 {
    
    static BigInteger p = new BigInteger("3a3d4c3d7e2a5d4c5c4d5b7e1c5a3c3e", 16);
    static BigInteger psi = new BigInteger("38532794441885460791256898927871100000");
    static BigInteger g = new BigInteger("91a812d65f3fea132099f2825312edbb", 16).mod(p);
    static BigInteger A = new BigInteger("16f2c65920ebeae43aabb5c9af923953", 16);    
    static BigInteger B = new BigInteger("3101c01f6b522602ae415d5df764587b", 16);
    static long[] q = new long[]{32L, 81L, 3125L, 7L, 37L, 61L, 73L, 113L, 389L, 4651L, 20175236914405679L};
 
    static int q_len = q.length;
    static HashSet[] xi = new HashSet[q_len];
    static BigInteger ai[] = new BigInteger[q_len];
    static HashSet res = new HashSet();
    
    static void rec(int ind)
    {
        if (ind == q_len)
        {
            BigInteger x = BigInteger.ZERO;
            for(int i=0;i<q_len;i++)
            {
                BigInteger mn = new BigInteger(((Long)q[i]).toString());
                BigInteger M = psi.divide(mn);
                x = x.add(ai[i].multiply(M).multiply(M.modInverse(mn)));
            }
            res.add(B.modPow(x.mod(psi), p));
            //res.add(x.mod(psi));
            return;
        }
        
        Iterator<Long> it = xi[ind].iterator();
        while(it.hasNext()){
            ai[ind] = new BigInteger(it.next().toString());
            rec(ind + 1);
        }      
    }
    
    public static void main(String[] args) {
 
        for(int i=0;i<q_len;i++)
        {
            xi[i] = new HashSet<Long>();
            long qi = q[i];
            int H = (int)Math.sqrt((double)qi) + 1;
                 
            BigInteger _a = g.modPow(psi.divide(new BigInteger(((Long)qi).toString())), p);
            BigInteger _b = A.modPow(psi.divide(new BigInteger(((Long)qi).toString())), p);
            
            BigInteger _c = _a.modPow(new BigInteger(((Integer)H).toString()), p);
            BigInteger _cp = _c;           
            int u_size = 1000000;
            
            boolean stop = false;
            for(int u_part = 1;u_part<=H && !stop;u_part+=u_size)
            {
                if (H > u_size) 
                {
                    System.out.print("[i] Processing ");
                    System.out.println(u_part);
                }
                TreeMap<BigInteger, Integer> table = new TreeMap<>();
                for(int u=u_part;u<=H && u<u_part + u_size;u++)
                {
                    table.put(_cp, u);
                    _cp = _cp.multiply(_c).mod(p);
                }
                BigInteger z = _b;
                for(int v=0;v<=H;v++)
                {
                    if (table.get(z) != null)
                    {
                        xi[i].add((((long)H)*table.get(z) - v) % qi);
                        stop = true;
                        break;
                    }
                    z = z.multiply(_a).mod(p);              
                }
                table.clear();
                System.gc();
            }
            System.out.println(xi[i].toString());
        } 
        rec(0);
        
        Iterator<BigInteger> it = res.iterator();
        while(it.hasNext()){
            System.out.println(it.next().toString(16));
        } 
    }
    
}
