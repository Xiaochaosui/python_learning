<%@ page   
        language="java"   
        import ="java.awt.*"  
        import ="java.awt.image.BufferedImage"  
        import ="java.util.*"  
        import ="javax.imageio.ImageIO"  
        pageEncoding="gb2312"%>  
<%  
    response.setHeader("Cache-Control", "no-cache");  
    int width=60,height=20;  
    BufferedImage bufferedImage=new BufferedImage(width,height,BufferedImage.TYPE_INT_RGB);  
    Graphics graphics=bufferedImage.getGraphics();  
    graphics.setColor(new Color(200,200,200));  
    graphics.fillRect(0, 0, width, height);  
    Random random=new Random();  
    int randnum=random.nextInt(8999)+1000;  
    String ranString=String.valueOf(randnum);  
    session.setAttribute("randStr", ranString);  
    graphics.setColor(Color.BLACK);  
    graphics.setFont(new Font("",Font.PLAIN,20));  
    graphics.drawString(ranString, 10, 17);  
    for(int i=0;i<100;i++){  
        int x=random.nextInt(width);  
        int y=random.nextInt(height);  
        graphics.drawOval(x, y, 1, 1);  
    }  
    ImageIO.write(bufferedImage, "JPEG", response.getOutputStream());  
    out.clear();  
    out=pageContext.pushBody();  
%>  