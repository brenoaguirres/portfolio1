using UnityEngine;

public class Billboard : MonoBehaviour
{
    private Transform spriteTransform;
    public Transform mainTransform;

    private void Start()
    {
        spriteTransform = GetComponent<SpriteRenderer>().transform;
        mainTransform = GetComponent<Transform>();
    }

    private void LateUpdate()
    {
        if (spriteTransform != null)
        {
            spriteTransform.LookAt(spriteTransform.position + Camera.main.transform.forward, Camera.main.transform.up);
        }

        mainTransform.rotation = Quaternion.identity;
    }
}