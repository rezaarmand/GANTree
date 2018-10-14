# GANTree

A hierarchical tree based architecture over Generative Adversarial Networks (GANs) for generation of samples from multi-modal distributions through discontinuous embedding manifold, having a flexibility to tweak the degree of interpolatability across the modes in the latent space.

```

GAN Tree Algorithm:

X = {0: all_x_data}

CREATE node0:
    node0.E = Encoder()
    node0.D = Decoder()
    node0.Di = Disc()
    
    node0.mu = [0, 0]
    node0.cov = [[1, 0], [0, 1]]

for node0: for each step:
    TRAIN node0.E and node0.D over cyclic_loss
    TRAIN node0.Di over disc_adv loss
    TRAIN node0.D over gen_adv loss
    
node0.gmm = GaussianMixture(n_components=2)
node0.gmm.fit(node0.encode(X[0]))
split X into 2 labels: 1 and 2

CREATE node1 and node2 from node0:
    E = node0.E.copy()
    node1.E = E
    node2.E = E
    
    node1.D = node0.D.copy()
    node2.D = node0.D.copy()
    
    node1.Di = node0.Di.copy()
    node2.Di = node0.Di.copy()
    
    node1.mu = node0.gmm.means_[0]
    node2.mu = node0.gmm.means_[1]
    
    node1.cov = node0.gmm.cov_[0]
    node2.cov = node0.gmm.cov_[1]

REPEAT for k iters: 
{
    REPEAT for a iters 
    {
        node = sample(node1, node2)
        
        z ~ N(node.mu, node.cov)
        x ~ X[node.id]
        
        TRAIN node.E and node.D over cyclic_loss
        TRAIN node.Di over disc_adv loss
        TRAIN node.D over gen_adv loss
        
        TRAIN node.E over x_clf_loss
    }
    
    z1 = node1.E(X[1])
    z2 = node2.E(X[2])
    
    gmm1 = GaussianMixture(n_components=1)
    gmm1.fit(z1)
    
    gmm2 = GaussianMixture(n_components=1)
    gmm2.fit(z2)
    
    node1.mu = gmm1.means_
    node2.mu = gmm2.means_
    
    node1.cov = gmm1.cov_
    node2.cov = gmm2.cov_
}

Generalize above in a recursive way for each split
```